# gportal-backup

Scheduled project to backup gportal games.

## Running

This project is setup to be executed by Github Actions.

The schedule and execution script is maintained within `.github/backup`.

## Development

Runs Selenium on local docker instance

```bash
docker run -d -p 4444:4444 --rm --shm-size 2g selenium/standalone-chrome
```
