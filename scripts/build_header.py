import re
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path


# all the knobs for the header live here, so nothing else needs touching if I want to tweak it later
header_hyperparams = {
    "github_username": "JBourton",
    "earliest_year_to_fetch": 2019,  # my 1st ever contribution was in 2019, so there's no point looking further back
    "curve_start_date": "2022-01-01",  # the x-axis starts here, but anything before still counts towards the running total
    "output_folder": "assets",
    "plot_left_x": 40,
    "plot_right_x": 800,
    "plot_bottom_y": 232,
    "plot_top_y": 150,
    "days_per_plotted_point": 7,  # 1 point per week keeps the path light whilst still looking smooth
    "draw_duration_seconds": 4.2,
    "light_theme": {"ink": "#1F2328", "muted": "#59636E", "accent": "#68246D", "rule": "#D0D7DE"},
    "dark_theme": {"ink": "#E6EDF3", "muted": "#8B949E", "accent": "#C9A3D4", "rule": "#30363D"},
}


# here I grab 1 year of the public contribution calendar & read the count out of each day's tooltip
def fetch_contributions_for_year(github_username, year):
    calendar_url= f"https://github.com/users/{github_username}/contributions?from={year}-01-01&to={year}-12-31"
    request_with_browser_agent= urllib.request.Request(calendar_url, headers={"User-Agent": "Mozilla/5.0"})
    calendar_html= urllib.request.urlopen(request_with_browser_agent, timeout=30).read().decode("utf-8")

    # GitHub keeps the date on the day cell & the actual count in a separate tooltip,
    # so I have to join the 2 together using the cell id.
    cell_id_to_date= {cell_id: day for day, cell_id in re.findall(r'data-date="(\d{4}-\d{2}-\d{2})" id="(contribution-day-component-[\d-]+)"', calendar_html)}
    contributions_for_this_year= {}
    for cell_id, tooltip_text in re.findall(r'<tool-tip[^>]*for="(contribution-day-component-[\d-]+)"[^>]*>([^<]*)</tool-tip>', calendar_html):
        count_match= re.match(r"(\d[\d,]*) contribution", tooltip_text)  # "No contributions on ..." just falls through to 0
        contributions_for_this_year[cell_id_to_date[cell_id]]= int(count_match.group(1).replace(",", "")) if count_match else 0
    return contributions_for_this_year


# this fetches every year from my earliest one up to now, skipping any year that fails instead of crashing the whole run
def fetch_all_contributions(github_username, earliest_year_to_fetch):
    all_contributions_by_date= {}
    for year_being_fetched in range(earliest_year_to_fetch, date.today().year + 1):
        try:
            all_contributions_by_date.update(fetch_contributions_for_year(github_username, year_being_fetched))
        except Exception as calendar_fetch_e:
            print(f"couldn't fetch {year_being_fetched}, so I'm skipping it ({calendar_fetch_e})")
    return all_contributions_by_date


# now I turn the daily counts into a running total, cutting it off at today so future calendar days don't flatten the end
def build_cumulative_points(all_contributions_by_date, curve_start_date, days_per_plotted_point):
    today_as_text= date.today().isoformat()
    days_up_to_today= sorted(day for day in all_contributions_by_date if day <= today_as_text)
    running_total= sum(all_contributions_by_date[day] for day in days_up_to_today if day < curve_start_date)
    cumulative_points= []
    for position, day in enumerate(day for day in days_up_to_today if day >= curve_start_date):
        running_total += all_contributions_by_date[day]
        if position % days_per_plotted_point == 0 or day == days_up_to_today[-1]:
            cumulative_points.append((day, running_total))
    return cumulative_points


# this maps the (date, total) pairs onto the header's plotting area & also works out where each year starts for the axis labels
def scale_points_to_header(cumulative_points, hyperparams):
    first_day= datetime.fromisoformat(cumulative_points[0][0])
    last_day= datetime.fromisoformat(cumulative_points[-1][0])
    total_span_in_days= max((last_day - first_day).days, 1)
    highest_total= max(total for _, total in cumulative_points)
    plot_width= hyperparams["plot_right_x"] - hyperparams["plot_left_x"]
    plot_height= hyperparams["plot_bottom_y"] - hyperparams["plot_top_y"]

    def x_for_day(day):
        return hyperparams["plot_left_x"] + ((day - first_day).days / total_span_in_days) * plot_width

    scaled_points= [(x_for_day(datetime.fromisoformat(day)), hyperparams["plot_bottom_y"] - (total / highest_total) * plot_height) for day, total in cumulative_points]
    year_tick_positions= [(year, x_for_day(datetime(year, 1, 1))) for year in range(first_day.year, last_day.year + 1) if datetime(year, 1, 1) >= first_day]
    return scaled_points, year_tick_positions, highest_total


# finally the svg itself, kept in the same paper-style layout as before so it still sits nicely under the title
def build_header_svg(scaled_points, year_tick_positions, highest_total, theme_colours, hyperparams):
    curve_path= "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in scaled_points)
    year_labels= "".join(f'<text class="y" x="{x:.1f}" y="247" text-anchor="middle">{year}</text><line x1="{x:.1f}" y1="{hyperparams["plot_bottom_y"]}" x2="{x:.1f}" y2="{hyperparams["plot_bottom_y"] + 4}" stroke="{theme_colours["rule"]}"/>' for year, x in year_tick_positions)
    draw_time= hyperparams["draw_duration_seconds"]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 272" width="840" height="272" role="img" aria-label="Joshua Bourton, with a graph of {highest_total:,} cumulative GitHub contributions">
<style>
.k{{font:600 11px 'Helvetica Neue',Helvetica,Arial,sans-serif;letter-spacing:2.6px;fill:{theme_colours["muted"]}}}
.t{{font:400 46px Georgia,'Times New Roman',Times,serif;fill:{theme_colours["ink"]}}}
.s{{font:italic 400 17px Georgia,'Times New Roman',Times,serif;fill:{theme_colours["muted"]}}}
.c{{font:italic 400 11px Georgia,'Times New Roman',Times,serif;fill:{theme_colours["muted"]}}}
.y{{font:400 10px Georgia,'Times New Roman',Times,serif;fill:{theme_colours["muted"]}}}
.n{{font:italic 400 12px Georgia,'Times New Roman',Times,serif;fill:{theme_colours["accent"]};opacity:0;animation:fade .8s ease-out {draw_time + 0.4}s forwards}}
.curve{{fill:none;stroke:{theme_colours["accent"]};stroke-width:2;stroke-linejoin:round;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:1;animation:draw {draw_time}s linear .4s forwards}}
.fade{{opacity:0;animation:fade 1s ease-out .2s forwards}}
@keyframes draw{{to{{stroke-dashoffset:0}}}}
@keyframes fade{{to{{opacity:1}}}}
</style>
<g class="fade">
<text class="k" x="40" y="34">DURHAM UNIVERSITY · DEPARTMENT OF COMPUTER SCIENCE</text>
<line x1="40" y1="46" x2="800" y2="46" stroke="{theme_colours["rule"]}" stroke-width="1"/>
<text class="t" x="38" y="100">Joshua Bourton</text>
<text class="s" x="40" y="130">Computational methods for political language, learning agents and data-driven systems</text>
<line x1="{hyperparams["plot_left_x"]}" y1="{hyperparams["plot_bottom_y"]}" x2="{hyperparams["plot_right_x"]}" y2="{hyperparams["plot_bottom_y"]}" stroke="{theme_colours["rule"]}" stroke-width="1" stroke-dasharray="3 4"/>
{year_labels}
<text class="c" x="800" y="266" text-anchor="end">Fig. 0. Cumulative GitHub contributions, refreshed daily from my contribution calendar</text>
</g>
<path id="curve" class="curve" pathLength="1" d="{curve_path}"/>
<circle r="3.5" fill="{theme_colours["accent"]}" opacity="0"><set attributeName="opacity" to="1" begin="0.4s"/><animateMotion dur="{draw_time}s" begin="0.4s" fill="freeze" calcMode="paced"><mpath href="#curve"/></animateMotion></circle>
<text class="n" x="{scaled_points[-1][0] - 8:.1f}" y="{scaled_points[-1][1] - 9:.1f}" text-anchor="end">{highest_total:,} contributions</text>
</svg>'''


if __name__ == "__main__":
    all_contributions_by_date= fetch_all_contributions(header_hyperparams["github_username"], header_hyperparams["earliest_year_to_fetch"])
    print(f"fetched {len(all_contributions_by_date)} calendar days & {sum(all_contributions_by_date.values())} contributions in total")

    cumulative_points= build_cumulative_points(all_contributions_by_date, header_hyperparams["curve_start_date"], header_hyperparams["days_per_plotted_point"])
    scaled_points, year_tick_positions, highest_total= scale_points_to_header(cumulative_points, header_hyperparams)

    output_folder= Path(header_hyperparams["output_folder"])
    output_folder.mkdir(exist_ok=True)
    for theme_name in ("light", "dark"):
        header_svg= build_header_svg(scaled_points, year_tick_positions, highest_total, header_hyperparams[f"{theme_name}_theme"], header_hyperparams)
        (output_folder / f"header-{theme_name}.svg").write_text(header_svg, encoding="utf-8")
    print(f"and wrote both headers with {len(scaled_points)} plotted points, ending on {highest_total:,}")
