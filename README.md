<h1 align="center">Cairo Transport</h1>

<p align="center">
  <strong>Smart-city transportation network optimization for Greater Cairo</strong><br>
  <sub>Graph algorithms · congestion prediction · interactive map dashboard</sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-1d1d26?style=for-the-badge&logo=python&logoColor=FFD60A" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-1d1d26?style=for-the-badge&logo=fastapi&logoColor=FFD60A" alt="FastAPI" />
  <img src="https://img.shields.io/badge/React-1d1d26?style=for-the-badge&logo=react&logoColor=FFD60A" alt="React" />
  <img src="https://img.shields.io/badge/NetworkX-1d1d26?style=for-the-badge&logoColor=FFD60A" alt="NetworkX" />
</p>

---

## Overview

Cairo Transport models Greater Cairo's districts and public facilities as graph nodes, roads as weighted edges, and traffic demand as time-dependent congestion data. The same algorithmic core runs through a command-line demo, a FastAPI backend and a React dashboard with interactive Leaflet maps.

## Algorithms

| Problem | Approach |
|:--|:--|
| Infrastructure planning | Modified Kruskal MST with mandatory critical nodes |
| Congestion-aware routing | Dijkstra, time-aware Dijkstra, memoized route planning |
| Emergency response | A* to the nearest facility with signal-preemption weights |
| Bus allocation & road maintenance | Dynamic programming |
| Traffic signals | Greedy optimization on flow-to-capacity ratios |
| Congestion forecasting | Linear regression (scikit-learn) |
| What-if analysis | Rush hour, road closures, emergencies, proposed roads |

## Tech stack

- **Backend:** Python · FastAPI · SQLite · NetworkX · Matplotlib · scikit-learn
- **Frontend:** React · TypeScript · Vite · Leaflet · Recharts · Framer Motion
- **Testing:** pytest (algorithms, graph, database, data validation, scenarios)
- **Deployment:** Docker Compose locally; Vercel (static frontend + Python API) in production

## Repository layout

```text
Cairo-Transport-main/      full project: algorithms, API, frontend, tests, docs
  cairo_transport/         graph model, algorithms, simulation, ML, visualizations
  frontend/                React + Vite dashboard
  tests/                   pytest suite
  docs/technical_report.md design and analysis write-up
api/index.py               Vercel serverless entry for the FastAPI app
vercel.json                Vercel build and routing
```

The detailed guide lives in [`Cairo-Transport-main/README.md`](Cairo-Transport-main/README.md), and the technical report in [`Cairo-Transport-main/docs/technical_report.md`](Cairo-Transport-main/docs/technical_report.md).

## Run locally

```bash
cd Cairo-Transport-main
docker compose up --build      # backend + frontend together
# or
pip install -r requirements-backend.txt && uvicorn api:app --reload
pytest
```

## Author

Built by **[Kerollos Nader](https://github.com/KerolosNader69)**.
