#!/bin/bash
umount /mnt/pico
mount /mnt/pico
cp kb.py main.py /mnt/pico
umount /mnt/pico
