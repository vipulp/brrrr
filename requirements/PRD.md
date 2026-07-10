"## The Twin-Engine Layout

The `/packages/financial-math` directory must remain dependency-free so it can compile via Pyodide/WASM into a client-side Web Worker on the front-end, while executing natively on the FastAPI backend.

## Universal Data Schema (UDS)

Layout tables for `uds_parcels` (spatial profiles), `uds_assessments` (tax profiles), and `uds_transactions_latest` (optimized latest transactional states).

## Geographic Pipeline Target Frameworks

Specifications for DuckDB vector geoprocessing of Washington King County and Snohomish County GIS shapefiles/GeoJSON layers, including a self-healing neighborhood median algorithm for malformed rows.

## Financial Underwriting Math Specifications

Implementation mandate for a Daily Precision Yield Matrix via a custom XIRR execution string, Interest-Only/Balloon/ARM advanced debt models, Straight-line 27.5-year depreciation modeling, and progressive Washington REET graduation modules.

## UI/UX & Local Storage Rules

Next.js 15 layout using shadcn/ui, Recharts visual maps, Maplibre GL WebGL mapping tiles, and Drizzle ORM + SQLite for an immutable "Credit Memo Baseline" frozen configuration tracking database.

## The 90-Day Roadmap Milestones

- Days 1-30: Pure Python Quant Core & Ingestion
- Days 31-60: DuckDB Aggregator & Pyodide WASM assembly
- Days 61-90: Reactive frontend interface & MIT-licensed release"