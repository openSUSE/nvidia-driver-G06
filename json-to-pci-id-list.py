#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Simone Caronni <negativo17@gmail.com>
# Licensed under the GNU General Public License Version or later

import json
import sys

def main():
    if len(sys.argv) != 3:
        print("usage: %s <driver version> supported-gpus.json" % sys.argv[0])
        return 1

    version = sys.argv[1]

    f = open(sys.argv[2])
    gpus_raw = json.load(f)


    devids_full = []
    devids_closed = []
    devids_open = []

    pci_ids_full = "pci_ids-" + version + ".full"
    pci_ids_closed = "pci_ids-" + version + ".closed"
    pci_ids_open = "pci_ids-" + version + ".open"

    for product in gpus_raw["chips"]:

        if "legacybranch" not in product.keys():

            gpu = product["devid"] + " " + product["name"]
            if not gpu in devids_full:
                devids_full.append(gpu)

        if "legacybranch" not in product.keys() and "kernelopen" not in product["features"]:

            gpu = product["devid"] + " " + product["name"]
            if not gpu in devids_closed:
                devids_closed.append(gpu)

        if "kernelopen" in product["features"]:

            gpu = product["devid"] + " " + product["name"]
            if not gpu in devids_open:
                devids_open.append(gpu)

    with open(pci_ids_full, "w") as file:
        for gpu in devids_full:
            file.write(gpu + '\n')
    print("Generated " + pci_ids_full + " (non-legacy)")

    with open(pci_ids_closed, "w") as file:
        for gpu in devids_closed:
            file.write(gpu + '\n')
    print("Generated " + pci_ids_closed + " (non-legacy, supported by closed modules only)")

    with open(pci_ids_open, "w") as file:
        for gpu in devids_open:
            file.write(gpu + '\n')
    print("Generated " + pci_ids_open + " (non-legacy, supported by open modules only)")

if __name__ == "__main__":
    main()
