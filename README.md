<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" alt="Joshua Bourton, Durham University, Department of Computer Science" width="100%">
</picture>

<p>
  <a href="https://www.linkedin.com/in/joshuabourton/"><img src="https://img.shields.io/badge/LinkedIn-joshuabourton-68246D?style=flat-square" alt="LinkedIn"></a>
  <a href="https://www.joshuabourton.uk"><img src="https://img.shields.io/badge/Interactive_CV-joshuabourton.uk-68246D?style=flat-square" alt="Interactive CV"></a>
  <a href="mailto:joshua.bourton16@gmail.com"><img src="https://img.shields.io/badge/Email-joshua.bourton16%40gmail.com-68246D?style=flat-square" alt="Email"></a>
</p>

<p><b><i>Abstract.</i></b> I am a First Class Computer Science graduate from Durham University, joining Accenture as a Technical Analyst. My academic work centres on computational methods for political language, using transformer models to quantify rhetoric at a scale that qualitative analysis cannot reach. Alongside this, I have built learning agents, generative models and real-time tracking systems under deliberately tight constraints. Every figure on this page is taken directly from that work.</p>

<p><b><i>Index Terms.</i></b> Natural language processing, transformers, reinforcement learning, generative modelling, sensor fusion, data engineering</p>

## 1&nbsp;&nbsp;Background

My route into industry ran through a year-long placement at Procter &amp; Gamble, where I worked as an IT project manager on internal data platforms. The role combined directing outsourced developers with hands-on delivery, including an ETL redesign, a Power BI to Databricks migration and application deployment on Azure App Service.

Alongside my degree, I have spent over seven years tutoring GCSE, A-level and IB Maths and Computer Science, which has shaped how I communicate technical work. I also evaluate large language model outputs on tool-calling and code-review tasks, and I am currently building a fully local, modular AI assistant on self-hosted hardware. Outside of computing I skydive, recording each jump in a [logbook app](https://github.com/JBourton/Skydiving-Logbook-App) I built for the purpose.

## 2&nbsp;&nbsp;Selected Work

### 2.1&nbsp;&nbsp;Dissertation &middot; [Securitising the Ballot](https://github.com/JBourton/Securitising-the-Ballot-Computational-Modelling-of-Securitising-Rhetoric-in-UK-Party-Manifestos)

*Computational modelling of securitising rhetoric in UK party manifestos*

My dissertation operationalises securitisation theory as a continuous, multi-dimensional regression problem. A shared DeBERTa-v3 encoder feeds three regression heads that score each manifesto sentence for threat, urgency and justification of extraordinary power. Because gold labels are costly to produce, auxiliary heads also learn from roughly 44,000 lexicon-derived pseudo-labels, supplementing 1,500 sentences that I annotated by hand.

The selected model reached a macro Spearman correlation of 0.524 and a macro QWK of 0.623 on held-out data, with 5-fold cross-validation confirming generalisation at 0.487 ± 0.016. Applied across six general elections from 2005 to 2024, it shows that securitising rhetoric diverged between parties. Threat became a shared baseline among the largest parties, urgency distinguished the governing party, and that party legislated most when its own securitising rhetoric was weakest.

<table>
  <tr>
    <td width="36%" align="center" valign="top">
      <img src="assets/secballot_architecture.png" width="250" alt="Multi-head DeBERTa regression architecture"><br>
      <sub><i>Fig. 1. Multi-head regression architecture, with auxiliary heads used only in training.</i></sub>
    </td>
    <td width="64%" align="center" valign="top">
      <img src="assets/secballot_heatmap.png" width="460" alt="Composite exceedance rate by party and election"><br>
      <sub><i>Fig. 2. Share of each manifesto's sentences above the composite securitisation threshold, with governing parties outlined.</i></sub>
    </td>
  </tr>
</table>

### 2.2&nbsp;&nbsp;Coursework and Projects

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="https://github.com/JBourton/The-Walking-Dead-Ends-RL-Locomotion"><img src="assets/walker_hardcore.gif" width="340" alt="TD3 walker clearing hardcore terrain"></a><br>
      <sub><i>Fig. 3. Hardcore run clearing stairs, stumps and pits.</i></sub>
      <p align="left"><b><a href="https://github.com/JBourton/The-Walking-Dead-Ends-RL-Locomotion">The Walking Dead-Ends</a></b><br><sub>YEAR 3 &middot; REINFORCEMENT LEARNING</sub><br>A TD3 agent that learns bipedal locomotion from scratch, extended for hardcore terrain with n-step returns, action smoothing and an episode-length curriculum. It averages 226 reward over its final 100 easy-mode episodes, whilst hardcore runs reach a median of 207 across the final 500.</p>
      <p align="left"><sub>PyTorch &middot; Gymnasium &middot; NumPy</sub></p>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="https://github.com/JBourton/vr-spatial-rotation-system"><img src="assets/bunny_rotation.gif" width="230" alt="Bunny rolling, pitching and yawing"></a><br>
      <sub><i>Fig. 4. Roll, pitch and yaw under the complementary filter.</i></sub>
      <p align="left"><b><a href="https://github.com/JBourton/vr-spatial-rotation-system">VR Spatial Rotation System</a></b><br><sub>YEAR 3 &middot; VIRTUAL REALITY</sub><br>Head tracking from raw IMU data, fusing gyroscope, accelerometer and magnetometer readings through quaternion complementary filters to drive a software-rendered Stanford bunny. Accelerometer fusion reduced roll drift at rest from 18.6° to 2.8° RMS.</p>
      <p align="left"><sub>NumPy &middot; OpenCV &middot; pandas</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="https://github.com/JBourton/Efficient-CIAFR-100-Deep-Learning"><img src="assets/cifar_gan_samples.jpg" width="230" alt="Class-conditional GAN samples"></a><br>
      <sub><i>Fig. 5. Uncurated class-conditional samples from the GAN.</i></sub>
      <p align="left"><b><a href="https://github.com/JBourton/Efficient-CIAFR-100-Deep-Learning">Efficient CIFAR-100 Modelling</a></b><br><sub>YEAR 3 &middot; DEEP LEARNING</sub><br>A MobileNet-inspired classifier that reaches 62.9% test accuracy within 100k parameters, paired with a projection-based conditional GAN that achieves an FID of 38.0 within 1M parameters. Both were built incrementally, retaining each change only where it measurably helped.</p>
      <p align="left"><sub>PyTorch &middot; clean-fid &middot; LPIPS</sub></p>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="https://github.com/JBourton/An-NLP-Analysis-of-Parliamentary-Attitudes-to-Public-Health-Pre-and-Post-Pandemic"><img src="assets/nlp_semantic_drift.png" width="340" alt="Semantic drift of party public-health framing"></a><br>
      <sub><i>Fig. 6. Semantic drift in each party's public-health framing, projected with PCA.</i></sub>
      <p align="left"><b><a href="https://github.com/JBourton/An-NLP-Analysis-of-Parliamentary-Attitudes-to-Public-Health-Pre-and-Post-Pandemic">Public Health Rhetoric Before and After COVID-19</a></b><br><sub>YEAR 3 &middot; NATURAL LANGUAGE PROCESSING</sub><br>Measures how four UK parties reframed public health between their 2019 and 2024 manifestos, combining bootstrapped VADER sentiment, SBERT semantic drift and POS-bigram stylistic analysis. Labour diverged most strongly, whilst the other three parties converged semantically.</p>
      <p align="left"><sub>sentence-transformers &middot; spaCy &middot; scikit-learn</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <a href="https://github.com/JBourton/Lumiere-Game"><img src="assets/lumiere.gif" width="300" alt="Lumiere Festival Planner gameplay"></a><br>
      <sub><i>Fig. 7. Placing light installations as visitors arrive, at roughly 4× speed.</i></sub>
      <p align="left"><b><a href="https://github.com/JBourton/Lumiere-Game">Lumiere Festival Planner</a></b><br><sub>YEAR 3 &middot; GAME DEVELOPMENT</sub><br>A browser-based management game set in Durham, in which autonomous visitors navigate using congestion-aware A* pathfinding. The player balances magic, staffing and crowd frustration through interlocking feedback loops, supported by a live congestion heatmap and accessibility features.</p>
      <p align="left"><sub>JavaScript &middot; Plotly &middot; HTML/CSS</sub></p>
    </td>
    <td width="50%" align="center" valign="top">
      <a href="https://github.com/JBourton/Image-Cleaning-For-Pneumonia-Diagnosis"><img src="assets/pneumonia_pipeline.gif" width="205" alt="X-ray cleaning pipeline stages"></a><br>
      <sub><i>Fig. 8. Each pipeline stage applied to a single scan.</i></sub>
      <p align="left"><b><a href="https://github.com/JBourton/Image-Cleaning-For-Pneumonia-Diagnosis">Image Cleaning for Pneumonia Diagnosis</a></b><br><sub>YEAR 2 &middot; COMPUTER VISION</sub><br>A classical computer vision pipeline that repairs noisy, warped and occluded chest X-rays before classification. Across 100 scans, cleaning raised a pre-trained classifier's accuracy from 55% to 93%.</p>
      <p align="left"><sub>OpenCV &middot; NumPy</sub></p>
    </td>
  </tr>
</table>

## 3&nbsp;&nbsp;Toolkit

<table>
  <tr>
    <td><b>Languages</b></td>
    <td align="center" width="76"><img src="assets/icons/python.svg" width="30" height="30" alt="Python"><br><sub>Python</sub></td>
    <td align="center" width="76"><img src="assets/icons/javascript.svg" width="30" height="30" alt="JavaScript"><br><sub>JavaScript</sub></td>
    <td align="center" width="76"><img src="assets/icons/typescript.svg" width="30" height="30" alt="TypeScript"><br><sub>TypeScript</sub></td>
    <td align="center" width="76"><img src="assets/icons/azuresql.svg" width="30" height="30" alt="SQL"><br><sub>SQL</sub></td>
    <td align="center" width="76"><img src="assets/icons/c.svg" width="30" height="30" alt="C"><br><sub>C</sub></td>
    <td align="center" width="76"><img src="assets/icons/html5.svg" width="30" height="30" alt="HTML5"><br><sub>HTML5</sub></td>
    <td align="center" width="76"><img src="assets/icons/css3.svg" width="30" height="30" alt="CSS3"><br><sub>CSS3</sub></td>
    <td align="center" width="76"><img src="assets/icons/latex.svg" width="30" height="30" alt="LaTeX"><br><sub>LaTeX</sub></td>
  </tr>
  <tr>
    <td><b>Machine learning</b></td>
    <td align="center"><img src="assets/icons/pytorch.svg" width="30" height="30" alt="PyTorch"><br><sub>PyTorch</sub></td>
    <td align="center"><img src="assets/icons/huggingface.svg" width="30" height="30" alt="Hugging Face"><br><sub>Hugging Face</sub></td>
    <td align="center"><img src="assets/icons/scikitlearn.svg" width="30" height="30" alt="scikit-learn"><br><sub>scikit-learn</sub></td>
    <td align="center"><img src="assets/icons/spacy.svg" width="30" height="30" alt="spaCy"><br><sub>spaCy</sub></td>
    <td align="center"><img src="assets/icons/opencv.svg" width="30" height="30" alt="OpenCV"><br><sub>OpenCV</sub></td>
    <td align="center"><img src="assets/icons/Farama-Foundation.png" width="30" height="30" alt="Gymnasium"><br><sub>Gymnasium</sub></td>
  </tr>
  <tr>
    <td><b>Data and statistics</b></td>
    <td align="center"><img src="assets/icons/pandas.svg" width="30" height="30" alt="pandas"><br><sub>pandas</sub></td>
    <td align="center"><img src="assets/icons/numpy.svg" width="30" height="30" alt="NumPy"><br><sub>NumPy</sub></td>
    <td align="center"><img src="assets/icons/scipy.svg" width="30" height="30" alt="SciPy"><br><sub>SciPy</sub></td>
    <td align="center"><img src="assets/icons/pysal.png" width="30" height="30" alt="PySAL"><br><sub>PySAL</sub></td>
    <td align="center"><img src="assets/icons/matplotlib.svg" width="30" height="30" alt="Matplotlib"><br><sub>Matplotlib</sub></td>
    <td align="center"><img src="assets/icons/seaborn.png" width="30" height="30" alt="seaborn"><br><sub>seaborn</sub></td>
    <td align="center"><img src="assets/icons/plotly.svg" width="30" height="30" alt="Plotly"><br><sub>Plotly</sub></td>
  </tr>
  <tr>
    <td><b>Cloud and DevOps</b></td>
    <td align="center"><img src="assets/icons/azure.svg" width="30" height="30" alt="Microsoft Azure"><br><sub>Azure</sub></td>
    <td align="center"><img src="assets/icons/appservice.svg" width="30" height="30" alt="Azure App Service"><br><sub>App Service</sub></td>
    <td align="center"><img src="assets/icons/docker.svg" width="30" height="30" alt="Docker"><br><sub>Docker</sub></td>
    <td align="center"><img src="assets/icons/githubactions.svg" width="30" height="30" alt="GitHub Actions"><br><sub>Actions</sub></td>
    <td align="center"><img src="assets/icons/git.svg" width="30" height="30" alt="Git"><br><sub>Git</sub></td>
  </tr>
  <tr>
    <td><b>Analytics and tooling</b></td>
    <td align="center"><img src="assets/icons/databricks.svg" width="30" height="30" alt="Databricks"><br><sub>Databricks</sub></td>
    <td align="center"><img src="assets/icons/powerbi.svg" width="30" height="30" alt="Power BI"><br><sub>Power BI</sub></td>
    <td align="center"><img src="assets/icons/jupyter.svg" width="30" height="30" alt="Jupyter"><br><sub>Jupyter</sub></td>
    <td align="center"><img src="assets/icons/colab.svg" width="30" height="30" alt="Google Colab"><br><sub>Colab</sub></td>
    <td align="center"><img src="assets/icons/vscode.svg" width="30" height="30" alt="VS Code"><br><sub>VS Code</sub></td>
  </tr>
</table>

## 4&nbsp;&nbsp;GitHub Activity

<p>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=JBourton&show_icons=true&hide_rank=true&hide=contribs&include_all_commits=true&hide_border=true&bg_color=00000000&title_color=C9A3D4&icon_color=C9A3D4&text_color=C9D1D9">
    <img height="165" src="https://github-readme-stats.vercel.app/api?username=JBourton&show_icons=true&hide_rank=true&hide=contribs&include_all_commits=true&hide_border=true&bg_color=00000000&title_color=68246D&icon_color=68246D&text_color=59636E" alt="GitHub stats">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=JBourton&layout=compact&langs_count=8&hide_border=true&bg_color=00000000&title_color=C9A3D4&text_color=C9D1D9">
    <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=JBourton&layout=compact&langs_count=8&hide_border=true&bg_color=00000000&title_color=68246D&text_color=59636E" alt="Top languages">
  </picture>
</p>
