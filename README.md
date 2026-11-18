# news-17-nov-2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/ItzSudhan/news-17-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/ItzSudhan/news-17-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

The world's news of Tuesday 17 November 2026 as one illustrated world map: 42 stories from six continents. Fifteen stories are drawn as vignettes pinned to where they happened, with the five biggest drawn largest: the Crimea bridge, Iran and the US in Bahrain and Hormuz, Trump at the Quad in Manila, Ebola in DR Congo and Russian strikes on Kyiv's bridges. The others are Gaza, the Knesset, Serbia's new parliament, measles in the Americas, Nvidia and Wall Street, Mongolia, COP31, Bangladesh's garment protests, Sudan and a military plane crash in Siberia. A numbered list below the map carries 27 more. Every story is checked against a news source in [`stories.md`](stories.md), and every illustration is an original inline-SVG drawing.

- `layout/map.html`: the page (HTML, CSS, inline SVG), rendered with headless Chrome by `render.sh`
- `layout/index.html`: the earlier panel-grid version of the same stories
- `entry.png`: the rendered image
- `main.py`: copies `entry.png` to `/output/entry.png` (Python 3.13, standard library only)

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=1pww8frk&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
