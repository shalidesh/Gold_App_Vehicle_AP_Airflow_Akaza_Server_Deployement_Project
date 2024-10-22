FROM postgres:13

# Copy the init.sh script to the docker-entrypoint-initdb.d directory
COPY init.sh /docker-entrypoint-initdb.d/init.sh

# Ensure the script has execute permissions
RUN chmod +x /docker-entrypoint-initdb.d/init.sh
