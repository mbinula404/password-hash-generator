# -*- coding: utf-8 -*-
import argparse  # import the module for parsing command-line arguments
import getpass  # import the module for reading input without echoing it to the screen
import hashlib  # import the module that provides hashing algorithms

SUPPORTED_ALGORITHMS = ["sha256", "sha512", "sha3_256", "blake2b", "md5"]  # list of hash algorithms the user may choose from


def build_parser():  # define a function that builds the argument parser
    parser = argparse.ArgumentParser(description="Hash a given password.")  # create the parser with a help description
    parser.add_argument("password", nargs="?", help="password to hash (omit to be prompted securely)")  # optional positional argument for the password
    parser.add_argument("-t", "--type", default="sha256", choices=SUPPORTED_ALGORITHMS, help="hash algorithm (default: sha256)")  # option to choose the algorithm
    parser.add_argument("-s", "--salt", default="", help="optional salt added before hashing")  # option to add a salt
    return parser  # return the finished parser


def hash_password(password, algorithm="sha256", salt=""):  # define a reusable function that computes the hash
    hasher = hashlib.new(algorithm)  # create a hash object for the chosen algorithm
    hasher.update((salt + password).encode("utf-8"))  # feed the salted password, as UTF-8 bytes, into the hasher
    return hasher.hexdigest()  # return the hash as a hexadecimal string


def main():  # define the main entry point
    args = build_parser().parse_args()  # parse the command-line arguments
    password = args.password if args.password is not None else getpass.getpass("Password: ")  # use the argument, or prompt hidden if missing
    digest = hash_password(password, args.type, args.salt)  # compute the hash
    print(f"< hash-type : {args.type} >")  # print which algorithm was used
    print(digest)  # print the resulting hash


if __name__ == "__main__":  # run only when executed directly, not when imported
    main()  # call the main function