"""Utilities launcher for the Codes/Python folder.

This script historically generated wallet CSV files. I added a small CLI
flag to optionally launch the GUI Flappy-style game from `gui_game.py`.

Usage:
    python run.py             # run the wallet CSV generator (original behavior)
    python run.py --launch flappy  # launch the Flappy GUI game

Note: wallet generation requires third-party packages (`solders`, `bip_utils`).
The GUI is imported lazily only when --launch flappy is requested to avoid
forcing those dependencies when the wallet tool is used.
"""

import os
import csv
import argparse
from solders.keypair import Keypair
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def generate_seed_phrase():
    """Generate a BIP39 seed phrase."""
    mnemonic = Bip39MnemonicGenerator().FromWordsNumber(12)  # Generate a 12-word mnemonic
    return mnemonic

def account_from_seed(seed_phrase):
    """Generate a keypair from a seed phrase."""
    seed_bytes = Bip39SeedGenerator(seed_phrase).Generate()
    bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA)
    bip44_acc = bip44_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
    return bip44_acc.PublicKey().ToAddress(), bip44_acc.PrivateKey().Raw().ToHex()

def main_wallet_generator():
    """Run the original wallet CSV generator.

    Prompts the user for a filename and number of accounts to generate, then
    writes addresses and seed phrases to a CSV file under ./Wallet.
    """
    name_file = str(input("Name Output file (without csv): "))
    amount = int(input("How many accounts to create: "))
    i = 0

    directory = "Wallet"
    create_directory_if_not_exists(directory)

    with open(file=os.path.join(directory, f"{name_file}.csv"), mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Address", "Seed Phrase"])  # Write header row
        while i != amount:
            seed_phrase = generate_seed_phrase()
            address, _ = account_from_seed(seed_phrase)
            print(f"Generated wallet {i+1}/{amount}: Address: {address}")
            writer.writerow([address, seed_phrase])
            i += 1


def main():
    parser = argparse.ArgumentParser(description="Run utilities in this folder")
    parser.add_argument('--launch', choices=['flappy'], help='Launch a GUI game (flappy)')
    args = parser.parse_args()

    if args.launch == 'flappy':
        # Import lazily to avoid introducing tkinter or GUI imports when the
        # user only wants the wallet generator. Any import or runtime errors
        # from the GUI code are surfaced here and printed rather than crashing
        # unexpectedly.
        try:
            from gui_game import main as launch_game
        except Exception as e:
            print("Failed to import gui_game:", e)
            return
        launch_game()
    else:
        main_wallet_generator()


if __name__ == '__main__':
    main()
