import analyzer
import report

temps = []

print("=== Multi-Sensor Temperature Analyzer ===")

num = int(input("How many sensor readings? "))

for i in range(num):

    temp = float(input(f"Enter temperature {i+1}: "))
    temps.append(temp)

avg, highest, lowest, status = analyzer.analyze_temperature(temps)

report.generate_report(avg, highest, lowest, status)