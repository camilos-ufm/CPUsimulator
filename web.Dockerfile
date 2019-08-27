#
# BudgetTracker Dockerfile for UI
#
FROM ubuntu:latest

USER root

RUN apt-get update
RUN apt-get install -y nginx nodejs

# Remove the default Nginx configuration file
RUN rm -v /etc/nginx/nginx.conf

# Copy a configuration file from the current directory
ADD nginx/nginx.conf /etc/nginx/
ADD nginx/mime.types /etc/nginx/

ADD /Simulator-Frontend/Unordered /usr/share/nginx/html/
ADD /Simulator-Frontend/Unordered /var/www/html/

# Append "daemon off;" to the beginning of the configuration
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Expose ports
#EXPOSE 90

# Set the default command to execute
# when creating a new container
CMD service nginx start
# FROM nginx

# #COPY /Simulator-Frontend /usr/share/nginx/html

# # Remove the default Nginx configuration file
# RUN rm -v /etc/nginx/nginx.conf

# # Copy a configuration file from the current directory
# ADD nginx.conf /etc/nginx/

# ADD /Simulator-Frontend /usr/share/nginx/html/
# ADD /Simulator-Frontend /var/www/html/

# # Append "daemon off;" to the beginning of the configuration
# RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# # Expose ports
# #EXPOSE 90

# # Set the default command to execute
# # when creating a new container
# CMD service nginx start
