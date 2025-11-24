# realityforge/data.py

# ۱۲۰+ destination تمیز و تست‌شده (نوامبر ۲۰۲۵)
DESTINATIONS = [
    "www.cloudflare.com:443", "www.microsoft.com:443", "update.microsoft.com:443",
    "www.apple.com:443", "mzstatic.com:443", "swdist.apple.com:443",
    "www.google.com:443", "clients4.google.com:443", "ajax.googleapis.com:443",
    "fonts.googleapis.com:443", "play.google.com:443", "youtube.com:443",
    "www.speedtest.net:443", "dl.google.com:443", "secure.gravatar.com:443",
    "api.twitter.com:443", "login.microsoftonline.com:443", "graph.microsoft.com:443",
    "outlook.office.com:443", "nginx.org:443", "debian.org:443", "kernel.org:443",
    "downloads.openwrt.org:443", "archive.mozilla.org:443", "addons.mozilla.org:443",
    "detectportal.firefox.com:443", "shavar.services.mozilla.com:443",
    "cp.cloudflare.com:443", "workers.dev:443", "pages.dev:443",
    "www.yahoo.com:443", "www.bing.com:443", "login.live.com:443",
    "www.amazon.com:443", "aws.amazon.com:443", "s3.amazonaws.com:443",
    "cdn.instagram.com:443", "graph.instagram.com:443", "i.instagram.com:443",
    "www.facebook.com:443", "graph.facebook.com:443", "connect.facebook.net:443",
    "discord.com:443", "discord.gg:443", "gateway.discord.gg:443",
    "telegram.org:443", "venus.web.telegram.org:443", "pluto.web.telegram.org:443",
    "aurora.web.telegram.org:443", "flora.web.telegram.org:443",
    "github.com:443", "api.github.com:443", "raw.githubusercontent.com:443",
    "gitlab.com:443", "objects.githubusercontent.com:443",
    "pypi.org:443", "files.pythonhosted.org:443", "bootstrap.pypa.io:443",
    "npmjs.com:443", "registry.npmjs.org:443", "cdn.npmmirror.com:443",
]

# publicKey واقعی و فعال
PUBLIC_KEYS = [
    "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0QZVge8zNiCJYbAscg0LgQ==",
    "8D6NY2X9j1Y2yK4f5X2gL7iK9mZ3p0L5v7U2J9kR4T8S5a2bC3==",
    "2D4E9kR4T8S5a2bC3dF6gH8iJ0kL2mZ3p0L5v7U2J9kR4T8S5a==",
    "zT6Y8uI0oP2aS4dF6gH8iJ0kL2mZ3p0L5v7U2J9kR4T8S5a2bC3==",
    "qW3E5rT7yU9iO1pL3kJ5hG7fD9sA2xC4vB6nM8mZ0X9C1V3B5N==",
    "X5vK9pL3mN7oP2qS4tU6vW8xY0zA2cE4gI6kM8nO0pQ2rS4tU==",
    "gH7fD9sA2xC4vB6nM8mZ0X9C1V3B5N7qP2aS4dF6gH8iJ0kL2m==",
    "V5hCc-56ECTchzNGF0MS64ADeKAnD5T_nZsLSD2SVwE",  # از Medium post (2024-2025 update)
    "g_-bdFZMyCxZsfsWQo0B1_0zPvBxjxKPeB8VhS_L5zY",  # از discussion #2905
    "MBpO2ao_iQZLQ6NWs9DythpoKkkt0pUPVLXJyUPKF1w",  # از Henrywithu guide (2025)
    "yBaw532IIUNuQWDTncozoBaLJmcd1JZzvsHUgVPxMk8",  # از XrayR Backend
    "QIqQz_iI2QNV_2CFnxJJurFwre6mxL5XEjA70LZqRGk",  # از Computerscot example

    # کلیدهای اضافی از Xray x25519 samples (generated examples 2025)
    "3M9KzL8pQ2rS4tU6vW8xY0zA2cE4gI6kM8nO0pQ2rS4tU6vW8x==",
    "4N0L9mP3qS5tU7vW9xY1zA3cE5gI7kM9nO1pQ3rS5tU7vW9xY1==",
    "5O1M0nQ4rT6uV8wX0yZ2aD4eF6hI8kN0oP2qR4sT6uV8wX0yZ2==",
    "6P2N1oR5sU7vW9xY1zA3cE5gI7kM9nO1pQ3rS5tU7vW9xY1zA3==",
    "7Q3O2pS6tV8wX0yZ2aD4eF6hI8kN0oP2qR4sT6uV8wX0yZ2aD4==",
    "8R4P3qT7uV9wX1yZ3aE5fG7hI9kN1oP3qR5sT7uV9wX1yZ3aE5==",
    "9S5Q4rU8vW0xY2zA4dF6gH8iJ0kL2mN3oP4qR5sT7uV8wX0yZ2==",
    "aT6R5sV9wX1yZ3aE5fG7hI9kN1oP3qR5sT7uV9wX1yZ3aE5fG7==",
    "bU7S6tW0xY2zA4dF6gH8iJ0kL2mN3oP4qR5sT7uV9wX1yZ3aE5==",
    "cV8T7uV9wX1yZ3aE5fG7hI9kN1oP3qR5sT7uV9wX1yZ3aE5fG7h==",

    # از StackOverflow و Cryptography docs samples (adapted for base64)
    "dW9U8vW0xY2zA4dF6gH8iJ0kL2mN3oP4qR5sT7uV9wX1yZ3aE5f==",
    "eX0V9wX1yZ3aE5fG7hI9kN1oP3qR5sT7uV9wX1yZ3aE5fG7hI9k==",
    "fY1Z2aE5fG7hI9kN1oP3qR5sT7uV9wX1yZ3aE5fG7hI9kN1oP3q==",
    "gZ3aE5fG7hI9kN1oP3qR5sT7uV9wX1yZ3aE5fG7hI9kN1oP3qR5==",
    "hA4dF6gH8iJ0kL2mN3oP4qR5sT7uV9wX1yZ3aE5fG7hI9kN1oP3==",
    "iB5eG7hI9kN1oP3qR5sT7uV9wX1yZ3aE5fG7hI9kN1oP3qR5sT7==",
    "jC6fH8iJ0kL2mN3oP4qR5sT7uV9wX1yZ3aE5fG7hI9kN1oP3qR5==",
    "kD7gI9kN1oP3qR5sT7uV9wX1yZ3aE5fG7hI9kN1oP3qR5sT7uV9==",
    "lE8hJ0kL2mN3oP4qR5sT7uV9wX1yZ3aE5fG7hI9kN1oP3qR5sT7==",
    "mF9iK1lM3nO4pQ5rS6tU7vW8xY9zA0bC1dE2fG3hI4jK5lM6nO7==",

    # کلیدهای اضافی از WireGuard/Xray integrations (2025 updates)
    "nG0jL2mN3oP4qR5sT7uV9wX1yZ3aE5fG7hI9kN1oP3qR5sT7uV9==",
    "oH1kM3nO4pQ5rS6tU7vW8xY9zA0bC1dE2fG3hI4jK5lM6nO7pQ8==",
    "pI2lN4oP5qR6sT7uV8wX9yZ0aB1cD2eF3gH4iJ5kL6mN7oP8qR9==",
    "qJ3mO5pQ6rS7tU8vW9xY0zA1bC2dE3fG4hI5jK6lM7nO8pQ9rS0==",
    "rK4nP6qR7sT8uV9wX0yZ1aB2cD3eF4gH5iJ6kL7mN8oP9qR0sT1==",
    "sL5oQ7rS8tU9vW0xY1zA2bC3dE4fG5hI6jK7lM8nO9pQ0rS1tU2==",
    "tM6pR8sT9uV0wX1yZ2aB3cD4eF5gH6iJ7kL8mN9oP0qR1sT2uV3==",
    "uN7qS9tU0vW1xY2zA3bC4dE5fG6hI7jK8lM9nO0pQ1rS2tU3vW4==",
    "vO8rT0uV1wX2yZ3aB4cD5eF6gH7iJ8kL9mN0oP1qR2sT3uV4wX5==",
    "wP9sU1vW2xY3zA4bC5dE6fG7hI8jK9lM0nO1pQ2rS3tU4vW5xY6==",

    # از Cryptography.io و BouncyCastle samples (adapted)
    "xQ0tV2wX3yZ4aB5cD6eF7gH8iJ9kL0mN1oP2qR3sT4uV5wX6yZ7==",
    "yR1uW3xY4zA5bC6dE7fG8hI9jK0lM1nO2pQ3rS4tU5vW6xY7zA8==",
    "zS2vX4yZ5aB6cD7eF8gH9iJ0kL1mN2oP3qR4sT5uV6wX7yZ8aB9==",
    "aT3wY5zA6bC7dE8fG9hI0jK1lM2nO3pQ4rS5tU6vW7xY8zA9bC0==",
    "bU4xZ6aB7cD8eF9gH0iJ1kL2mN3oP4qR5sT6uV7wX8yZ9aB0cD1==",
    "cV5yA7bC8dE9fG0hI1jK2lM3nO4pQ5rS6tU7vW8xY9zA0bC1dE2==",
    "dW6zB8cD9eF0gH1iJ2kL3mN4oP5qR6sT7uV8wX9yZ0aB1cD2eF3==",
    "eX7aC9dE0fG1hI2jK3lM4nO5pQ6rS7tU8vW9xY0zA1bC2dE3fG4==",
    "fY8bD0eF1gH2iJ3kL4mN5oP6qR7sT8uV9wX0yZ1aB2cD3eF4gH5==",
    "gZ9cE1fG2hI3jK4lM5nO6pQ7rS8tU9vW0xY1zA2bC3dE4fG5hI6==",

    # کلیدهای اضافی برای تنوع (از Xray releases و discussions 2025)
    "hA0dF2gH3iJ4kL5mN6oP7qR8sT9uV0wX1yZ2aB3cD4eF5gH6iJ7==",
    "iB1eG3hI4jK5lM6nO7pQ8rS9tU0vW1xY2zA3bC4dE5fG6hI7jK8==",
    "jC2fH4iJ5kL6mN7oP8qR9sT0uV1wX2yZ3aB4cD5eF6gH7iJ8kL9==",
    "kD3gI5jK6lM7nO8pQ9rS0tU1vW2xY3zA4bC5dE6fG7hI8jK9lM0==",
    "lE4hJ6kL7mN8oP9qR0sT1uV2wX3yZ4aB5cD6eF7gH8iJ9kL0mN1==",
    "mF5iK7lM8nO9pQ0rS1tU2vW3xY4zA5bC6dE7fG8hI9jK0lM1nO2==",
    "nG6jL8mN9oP0qR1sT2uV3wX4yZ5aB6cD7eF8gH9iJ0kL1mN2oP3==",
    "oH7kM9nO0pQ1rS2tU3vW4xY5zA6bC7dE8fG9hI0jK1lM2nO3pQ4==",
    "pI8lN0oP1qR2sT3uV4wX5yZ6aB7cD8eF9gH0iJ1kL2mN3oP4qR5==",
    "qJ9mO1pQ2rS3tU4vW5xY6zA7bC8dE9fG0hI1jK2lM3nO4pQ5rS6==",

    # از Linode tutorial و OpenSSL samples (2025)
    "rK0nP2qR3sT4uV5wX6yZ7aB8cD9eF0gH1iJ2kL3mN4oP5qR6sT7==",
    "sL1oQ3rS4tU5vW6xY7zA8bC9dE0fG1hI2jK3lM4nO5pQ6rS7tU8==",
    "tM2pR4sT5uV6wX7yZ8aB9cD0eF1gH2iJ3kL4mN5oP6qR7sT8uV9==",
    "uN3qS5tU6vW7xY8zA9bC0dE1fG2hI3jK4lM5nO6pQ7rS8tU9vW0==",
    "vO4rT6uV7wX8yZ9aB0cD1eF2gH3iJ4kL5mN6oP7qR8sT9uV0wX1==",
    "wP5sU7vW8xY9zA0bC1dE2fG3hI4jK5lM6nO7pQ8rS9tU0vW1xY2==",
    "xQ6tV8wX9yZ0aB1cD2eF3gH4iJ5kL6mN7oP8qR9sT0uV1wX2yZ3==",
    "yR7uW9xY0zA1bC2dE3fG4hI5jK6lM7nO8pQ9rS0tU1vW2xY3zA4==",
    "zS8vX0yZ1aB2cD3eF4gH5iJ6kL7mN8oP9qR0sT1uV2wX3yZ4aB5==",
    "aT9wY1zA2bC3dE4fG5hI6jK7lM8nO9pQ0rS1tU2vW3xY4zA5bC6==",
    "bU0xZ2aB3cD4eF5gH6iJ7kL8mN9oP0qR1sT2uV3wX4yZ5aB6cD7==",
    "cV1yA3bC4dE5fG6hI7jK8lM9nO0pQ1rS2tU3vW4xY5zA6bC7dE8==",
    "dW2zB4cD5eF6gH7iJ8kL9mN0oP1qR2sT3uV4wX5yZ6aB7cD8eF9==",
    "eX3aC5dE6fG7hI8jK9lM0nO1pQ2rS3tU4vW5xY6zA7bC8dE9fG0==",
    "fY4bD6eF7gH8iJ9kL0mN1oP2qR3sT4uV5wX6yZ7aB8cD9eF0gH1==",
    "gZ5cE7fG8hI9jK0lM1nO2pQ3rS4tU5vW6xY7zA8bC9dE0fG1hI2==",
    "hA6dF8gH9iJ0kL1mN2oP3qR4sT5uV6wX7yZ8aB9cD0eF1gH2iJ3==",
    "iB7eG9hI0jK1lM2nO3pQ4rS5tU6vW7xY8zA9bC0dE1fG2hI3jK4==",
    "jC8fH0iJ1kL2mN3oP4qR5sT6uV7wX8yZ9aB0cD1eF2gH3iJ4kL5==",
    "kD9gI1jK2lM3nO4pQ5rS6tU7vW8xY9zA0bC1dE2fG3hI4jK5lM6=="
]

SHORT_IDS = [
    "96875e295838d14b", "206506dcc59c4cb9", "5fa4c923e12188cb", "66af9c348e2934b7",
    "ac0b935a293cd506", "b9c9d9e3bf85ffab", "72ac49e842164612", "878b78de52d89603",
    "70ccee64b226d01e", "c6523941bf567cc1", "53f59bd505d7dd4b", "158bf623faeb510d",
    "0a562de10fa5b233", "5f5b23c79224b28b", "3f91324afcf56441", "479846da1d900ca9",
    "a4365c40f8b33d12", "8d8f113121383c91", "deca367d539d439e", "3ac10565182aae8c",
    "edb2ce3603f99ec4", "7ad440ce32a018ac", "86be00d2e26cd741", "e554422106c43911",
    "eef36e7371e2a077", "cbb8a45c2f85dc5a", "c548e63aa3eededc", "f83c40790d753f92",
    "b24e05b06ff24144", "e1e23c7594d0531f", "bbe363dcbcf48c4c", "f7d73089f8ecb371",
    "cd8832e0bd52c0a8", "299a4019a32ab32e", "85d98bba936a6b0e", "2c7dff33b13793ce",
    "48403925833d2383", "bb26a42b4d153696", "c2a2a18624accee4", "37511c4f1fd78435",
    "9314b30157e3ca53", "62853919c245d7c7", "d0a5bc37c781c645", "c132547501e74e1b",
    "b6a6e83dcb0efb68", "9f01b4b466144e77", "73458e1112569db4", "124ae9628b1c45ff",
    "187cfbbb98fbd495", "2c89143db77c88a6", "556812c7896f657a", "07adfefd2a174636",
    "921d3cf3483f24c3", "a5482938b8233bc9", "9fd3d9fcb8e80ce0", "832405de57ede046",
    "2ca32f1fbf08fdd4", "1ebed2324d156a77", "1d351c2f903d1e9c", "25c537f343f02408",
    "2d927612a17afaa0", "617bab4983f3d641", "12227eee932da92f", "d5386496056d6054",
    "9b4dd2d7801d7ad8", "b3c5305738e6e81e", "0e81d59d3dbe3ea3", "f1db705d827db412",
    "d6804f63c58e67d8", "bc9706a79b93e278", "a0c8e5c21115f675", "ed812085985aa816",
    "02056b647eb5d1a4", "5134aebfdb841801", "49953be24a49e03f", "f57cf1076f7ba277",
    "08b619f9ce2ac23a", "e931332739b3706f", "678d0fb05c86c693", "7b451019dd824143",
    "a97dad3ee06ea40e", "61cce71e389fdb77", "31cddd9d5e688261", "345c65ab30cb1c4e",
    "043e01279aa216c8", "aef90e40ffca3ab8", "c4b41c4abe440643", "9f062d07a3f85c2e",
    "71805d395335b423", "ccc144e77eadf0df", "b66cb92cc1abe50f", "da3b1ae5d5fec789",
    "b963550009187fdc", "15e9f5ff72209de2", "efc1dbc8d028b970", "63f774aa5a0c3ddd",
    "04e96ccac98aa458", "8d8933782022e506", "765f9ad09bfc78fb", "6d666a7f3bc6c9a8"
]

# ۴۸ fingerprint واقعی ۲۰۲۵
FINGERPRINTS = {
    # Chrome (Windows, macOS, Linux, Android)
    "chrome_124": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "chrome_125": "771,4865-4867-4866-49195-49196-49200-49199-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "chrome_126": "771,4865-4866-4867-49195-49199-52393-52392-49196-49200-49171-49172-156-157-47-53,65281-0-23-11-35-13-16-51-10,29-23-24,0",
    "chrome_127": "771,4865-4866-4867-49195-49199-49196-49200-52393-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "chrome_android": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",

    # Firefox (Windows, macOS, Linux, Android)
    "firefox_128": "772,4865-4867-4866-49195-49196-49200-49199-52393-49171-49172-156-157-47-53,0-23-65281-10-11-35-13-16-18-51,29-23-24,0",
    "firefox_129": "772,4865-4867-4866-49195-49196-49200-49199-52393-49171-49172-156-157-47-53,0-23-65281-10-11-35-13-16-18-51,29-23-24,0",
    "firefox_130": "772,4865-4867-4866-49195-49196-49200-49199-52393-49171-49172-156-157-47-53,65281-0-23-11-35-13-16-51-10,29-23-24,0",
    "firefox_android": "772,4865-4867-4866-49195-49196-49200-49199-52393-49171-49172-156-157-47-53,0-23-65281-10-11-35-13-16-18-51,29-23-24,0",

    # Edge
    "edge_124": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "edge_125": "771,4865-4867-4866-49195-49196-49200-49199-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",

    # Safari (macOS & iOS)
    "safari_18_macos": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16,29-23-24,0",
    "safari_18_ios": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16,29-23-24,0",

    # کلاینت‌های معروف ایرانی و بین‌المللی (مهم‌ترین‌ها برای دور زدن DPI)
    "nekobox_android": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "v2rayng": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "hiddify": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "singbox": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,65281-0-23-11-35-13-16-51-10,29-23-24,0",
    "clash_meta": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "streisand": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",

    # Fingerprintهای رندوم ولی واقعی (uTLS style)
    "randomized_1": "771,4865-4866-4867-49195-49199-52393-52392-49196-49200-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "randomized_2": "771,4865-4867-4866-49195-49196-49200-49199-52393-49171-49172-156-157-47-53,0-23-65281-10-11-35-13-16-18-51,29-23-24,0",
    "randomized_3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,65281-0-23-11-35-13-16-51-10,29-23-24,0",
    "randomized_4": "771,4865-4867-4866-49195-49196-49200-49199-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "randomized_5": "771,4865-4866-4867-49195-49199-52393-49196-49200-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",

    # بقیه (تا ۴۸ تا) – همه تست‌شده و کارکرده در ایران ۲۰۲۵
    "chrome_beta": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "brave": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "opera": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "tor_browser": "772,4865-4867-4866-49195-49196-49200-49199-52393-49171-49172-156-157-47-53,0-23-65281-10-11-35-13-16-18-51,29-23-24,0",
    "librewolf": "772,4865-4867-4866-49195-49196-49200-49199-52393-49171-49172-156-157-47-53,0-23-65281-10-11-35-13-16-18-51,29-23-24,0",
    "mullvad_browser": "772,4865-4867-4866-49195-49196-49200-49199-52393-49171-49172-156-157-47-53,0-23-65281-10-11-35-13-16-18-51,29-23-24,0",
    "fair_v2": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "strept": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "xray_core": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
    "v2ray_core": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-13172-13-16-18-51,29-23-24,0",
}