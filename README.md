# Password Hash Generator

A simple command-line Python tool that generates password hashes using different hashing algorithms. Supports optional salt and secure password input.

## Features

- Generate password hashes.
- Support multiple hashing algorithms.
- Optional salt support.
- Hidden password input using `getpass`.
- Command-line arguments using `argparse`.
- No external dependencies required.

## Requirements

- Python 3.x

All required modules are included in Python's standard library.

## Project Structure

```text
PasswordHashGenerator/
│
└── password_hash.py
```

## Usage

Open CMD or PowerShell in the project directory.

### 1. Run the program

```bash
python password_hash.py
```

You will be prompted to enter your password securely.

### 2. Provide a password directly

```bash
python password_hash.py MyPassword123
```

### 3. Select a hashing algorithm

Use `-t` or `--type` to choose an algorithm.

```bash
python password_hash.py MyPassword123 -t sha512
```

### 4. Add a salt

Use `-s` or `--salt` to provide an optional salt.

```bash
python password_hash.py MyPassword123 -s RandomSalt123
```

### 5. Combine algorithm and salt

```bash
python password_hash.py MyPassword123 -t sha256 -s RandomSalt123
```

### 6. Display help

```bash
python password_hash.py -h
```

## Supported Algorithms

| Algorithm | Hash Size |
|---|---:|
| SHA-256 | 256 bits |
| SHA-512 | 512 bits |
| SHA3-256 | 256 bits |
| BLAKE2b | 512 bits |
| MD5 | 128 bits |

The default algorithm is `sha256`.

## Example Output

```text
< hash-type : sha256 >
[Generated hexadecimal hash]
```

The actual hash depends on the password, algorithm, and salt.

## Security Notice

This project is intended for educational purposes and learning cryptographic hashing.

- MD5 is not recommended for security-sensitive applications.
- SHA-256 and SHA-512 are not suitable for direct password storage.
- The optional salt in this program is manually provided and is not automatically generated.
- For real-world password storage, use password hashing algorithms such as Argon2id, bcrypt, or scrypt.

## License

This project is available for educational and personal use.