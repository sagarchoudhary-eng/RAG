CREATE TABLE document (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    source VARCHAR(100),
    department VARCHAR(100),
    document_type VARCHAR(50),
    access_level VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE document_version (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    document_id BIGINT NOT NULL
        REFERENCES document(id) ON DELETE CASCADE,

    version INT NOT NULL,
    checksum VARCHAR(64) NOT NULL UNIQUE,

    status VARCHAR(50) NOT NULL DEFAULT 'PROCESSING'
        CHECK (status IN (
            'UPLOADED',
            'PROCESSING',
            'INDEXING',
            'READY',
            'FAILED'
        )),

    is_active BOOLEAN NOT NULL DEFAULT FALSE,

    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT uq_document_version
        UNIQUE (document_id, version)
);

CREATE UNIQUE INDEX uq_active_document_version
ON document_version (document_id)
WHERE is_active = TRUE;


CREATE TABLE chunk (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    document_version_id BIGINT NOT NULL
        REFERENCES document_version(id) ON DELETE CASCADE,

    text TEXT NOT NULL,

    embedding_model VARCHAR(100),
    embedding_model_version VARCHAR(50),
    embedding_dimension INT,

    chunk_index INT NOT NULL,
    page_number INT,
    section VARCHAR(255),

    CONSTRAINT uq_version_chunk
        UNIQUE (document_version_id, chunk_index)
);