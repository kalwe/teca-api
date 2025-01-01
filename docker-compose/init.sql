DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'coif') THEN
      CREATE DATABASE coif
      WITH
      ENCODING = 'UTF8'
      CONNECTION LIMIT -1;
   END IF;
   GRANT ALL PRIVILEGES ON DATABASE agil TO docker;
END
$$;
