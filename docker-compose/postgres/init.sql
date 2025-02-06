DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'teca_coif') THEN
      CREATE DATABASE teca_coif
      WITH
      ENCODING = 'UTF8'
      CONNECTION LIMIT -1;
   END IF;
   GRANT ALL PRIVILEGES ON DATABASE teca_coif TO docker;
END
$$;
