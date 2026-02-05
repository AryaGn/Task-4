DROP TABLE IF EXISTS company_web_enrichment CASCADE;
DROP TABLE IF EXISTS scrape_runs CASCADE;
DROP TABLE IF EXISTS company_snapshots CASCADE;
DROP TABLE IF EXISTS companies CASCADE;

CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    yc_company_id TEXT UNIQUE,
    name TEXT,
    domain TEXT,
    first_seen_at TIMESTAMP,
    last_seen_at TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE company_snapshots (
    id SERIAL PRIMARY KEY,
    company_id INTEGER REFERENCES companies(id),
    batch TEXT,
    stage TEXT,
    description TEXT,
    location TEXT,
    tags JSONB,
    employee_range TEXT,
    scraped_at TIMESTAMP,
    data_hash TEXT
);

CREATE TABLE company_web_enrichment (
    id SERIAL PRIMARY KEY,
    company_id INTEGER REFERENCES companies(id),
    has_careers_page BOOLEAN,
    has_blog BOOLEAN,
    contact_email TEXT,
    scraped_at TIMESTAMP
);

CREATE TABLE scrape_runs (
    id SERIAL PRIMARY KEY,
    started_at TIMESTAMP,
    ended_at TIMESTAMP,
    total_companies INTEGER,
    new_companies INTEGER,
    updated_companies INTEGER,
    unchanged_companies INTEGER,
    failed_companies INTEGER,
    avg_time_per_company_ms INTEGER
);
