awk 'NR==1 {print($0)}' test.py
sed -n '1p' test.py