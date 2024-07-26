#!/usr/bin/python3
from brownie import SuperCoin, accounts

def main():
    acct = accounts.load("defac", password="def123")
    response = SuperCoin.deploy({'from': acct})
