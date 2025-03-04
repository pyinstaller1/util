
cd C:\Users\%USERNAME%

powershell -Command "Start-Process cmd -ArgumentList '/k python touch.py' -Verb RunAs"
