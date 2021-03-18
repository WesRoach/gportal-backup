# gportal-backup

Scheduled project to backup gportal games.

## Running

This project is configured to run via Github Actions.

Manual Backup and Scheduled Backup Github Actions are within `.github/backup`.

1. Fork this repository.
1. Create the following Github secret key-value pairs within your fork's Github page.
   - GPORTAL_EMAIL
   - GPORTAL_PASSWORD
     - Username/Password: You'll need to configure Gportal to login with a username/password rather than an OAuth provider such as Google, Facebook, etc
   - GPORTAL_BACKUP_URL
     - This is the URL from the "Backup" page within Gportal.
     - Ex: `https://www.g-portal.com/int/server/valheim/123456/system/backup`
1. Test your setup using the Github Action: "Manual Backup"
1. "Scheduled Backup" is set to run every day at 4AM - this value is configurable
   - [https://crontab.guru/every-day-at-4am](https://crontab.guru/every-day-at-4am)

## Development

Runs Selenium on local docker instance

```bash
docker run -d -p 4444:4444 --rm --shm-size 2g selenium/standalone-chrome
```
