#!/bin/sh

# wait for Elasticsearch to start, then run the setup script to
# create and configure the index.
echo "Waiting for Elasticsearch"
exec /utils/wait-for-it.sh localhost:9200 -- /usr/local/bin/elasticsearch/add_index_template.sh &
exec $@

echo "Waiting for postgres"

while ! nc -z web-db 5432; do
    sleep 0.1
done

echo "PostgreSQL started"

exec "$@"
