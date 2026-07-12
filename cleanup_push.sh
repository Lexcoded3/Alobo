#!/bin/bash
cd "C:/xampp/htdocs/2026/Alobo"

echo "=== Cleaning temp files ==="
rm -f check_images.py optimize_images.py nul
rm -rf assets/_originals/

echo "=== Staging all changes ==="
git add -A

echo "=== Committing ==="
git commit -m "Optimize images: convert large PNGs to JPEG, fix broken srcset, compress assets (6.2MB -> 3.2MB)"

echo "=== Pushing ==="
git push origin main
