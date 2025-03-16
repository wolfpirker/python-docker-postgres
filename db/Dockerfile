FROM postgres:13-alpine

# Copy initialization script and helper scripts
COPY init.sql /docker-entrypoint-initdb.d/
COPY scripts/ /scripts/
RUN chmod +x /scripts/*.sh

# Set entrypoint to check for existing data
ENTRYPOINT ["./scripts/check_existing_data.sh"]
CMD ["postgres"]
