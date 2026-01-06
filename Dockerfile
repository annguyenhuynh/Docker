# Base image
FROM alpine:3.18

RUN apk add curl

# the directory is Linux-based style, and will be created if none exists
WORKDIR /src/demo

# Add user
RUN adduser -D cloudchamp

USER cloudchamp

ENV APP_ENV=dev \
    LOG_LEVEL=debug \
    TIMEOUT=30

# Copy <src> <dest>
COPY app.py /src/demo/

# Expose port(s) apps should listen to
EXPOSE 5000

# Using CMD
CMD ["flask", "run", "--host-0.0.0.0", "--port=5000"]









