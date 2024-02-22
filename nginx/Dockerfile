# Use the official Nginx image
FROM nginx:latest

# Remove the default configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom Nginx configuration
COPY nginx/nginx.conf /etc/nginx/conf.d/

# Set the working directory to /app
WORKDIR /app

# Expose port 80 to the world outside this container
EXPOSE 80

# Define the command to run Nginx
CMD ["nginx", "-g", "daemon off;"]
