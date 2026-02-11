# FreeFire API Manager

A powerful API for managing FreeFire accounts and friends.

## Features

- Add friends to FreeFire accounts
- Remove friends from FreeFire accounts
- Get player information
- Generate JWT tokens
- Cross-platform compatibility

## Endpoints

- `/add_friend` - Add a friend using UID/password or token
- `/remove_friend` - Remove a friend using UID/password or token
- `/get_player_info` - Get player information
- `/token` - Generate JWT token from UID/password
- Utility endpoints: `/health`, `/status`, `/version`, `/metrics`, `/info`

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## Deployment to Vercel

This application is ready for deployment to Vercel. Simply connect your GitHub repository to Vercel and it will automatically deploy.

### Manual Deployment Steps:
1. Install the Vercel CLI: `npm i -g vercel`
2. Run `vercel` in this directory
3. Follow the prompts to deploy

### Or Deploy Directly:
[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/your-repo)

## Usage Examples

### Add Friend
```
GET /add_friend?player_id=TARGET_UID&uid=YOUR_UID&password=YOUR_PASSWORD
```

### Get Player Info
```
GET /get_player_info?player_id=TARGET_UID&uid=YOUR_UID&password=YOUR_PASSWORD
```

### Generate Token
```
GET /token?uid=YOUR_UID&password=YOUR_PASSWORD
```

## Configuration

The application uses protobuf files for communication with FreeFire servers and includes retry mechanisms for reliable operations.

## Security

- Implements AES encryption for sensitive data
- Supports CORS for web applications
- Includes rate limiting protection

## License

This project is for educational purposes only.
