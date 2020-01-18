# FunTOTP
A simple and secure 2FA command-line client in Python

With this, you can use 2FA with any account. It's simple code and you secrets will stay safe because the TOTP secrets are stored in a encrpted file, the plaintext never touch the computer's hard drive. Inspired by [susam/mintotp](https://github.com/susam/mintotp) and [dlorch/toytotp](https://github.com/dlorch/toytotp).

**NOTE:** This repository is considered good for beginners, especially in Python. The only previous knowledge to modify and contribute with this code is the basics of Object Oriented Programming (OOP) and its implementation in Python.

**THIS IS VULNERABLE TO SIDE-CHANNEL ATTACKS AND ANY PERSON WITH PHYSICAL ACCESS TO YOUR COMPUTER WHILE THE PROGRAM IT'S RUNNING CAN GET THE KEYS**

## Built With
This is a Python 3 code that uses [Fernet](https://cryptography.io/en/latest/fernet/) for encryption with Whirlpool hash as Salt. For generate the 6-digits TOTP, use [susam/mintotp](https://github.com/susam/mintotp) as a module.

## Getting Started

You can use the program in three ways: using python interpreter, compiling a binary and install in you system.

### Prerequisites
- git
- python3
- pip

### Installation

```bash
git clone https://github.com/Z33DD/FunTOTP.git
cd FunTOTP
```
Here you choose how you want to use the program, just run it with the interpreter, compile a binary for faster execution or install the program so you can use it as a command in the terminal.

To just run the program, execute it
```bash
./funtotp
```

To compile, it has a script ready for this task in Scripts/compile
```bash
cp Scripts/compile ./compile
./compile
```
A executable funtotp.bin file will be generated

Finnally, if you want to install, use the install script
```bash
./install
```

### Running the tests

For the tests to work correctly, move or copy them from Tests/ to the project's directory.

```bash
cp * ../
```

After, execute one by one:

```bash
cd ..
python3 AES256_test.py
python3 keystore_test.py
```

In case of any problems, create a Issue


### Usage

```
❯ ./funtotp --help
usage: FunTOTP [-h] [--version] [--secret SECRET] [--keystore KEYSTORE]
               [--erase] [--newkey] [--remove REMOVE] [--printkeys]

TOTP encrypted keychain

optional arguments:
  -h, --help            show this help message and exit
  --version, -v         show program's version number and exit
  --secret SECRET       Add a new TOTP Key
  --keystore KEYSTORE, -k KEYSTORE
                        Set the keystore file
  --erase, -e           This will DELETE ALL KEYS, are you sure?
  --newkey              Interactive guide to give you a help
  --remove REMOVE       Remove a key by title
  --printkeys           Print the TOTPs

Make by Z33DD with love
```

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests. Any and all contributions are welcome.

## License

This project is licensed under the Unlicense - see the LICENSE.md file for details
