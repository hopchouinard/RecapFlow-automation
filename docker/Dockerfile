FROM n8nio/n8n:latest

# Set environment variables
ENV N8N_HOST=localhost
ENV N8N_PORT=5678
ENV N8N_PROTOCOL=http
ENV N8N_BASIC_AUTH_ACTIVE=false
ENV N8N_BASIC_AUTH_USER=
ENV N8N_BASIC_AUTH_PASSWORD=
ENV N8N_DB_TYPE=sqlite
ENV N8N_DB_SQLITE_DATABASE=/data/database.sqlite

# Install any additional dependencies if needed
# RUN npm install <additional-dependencies>

# Expose the port
EXPOSE 5678

# Command to run n8n
CMD ["n8n", "start"]