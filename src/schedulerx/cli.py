import argparse, json
from datetime import datetime
from .adapters_csv import CSVOrdersLoader, CSVResourcesLoader, CSVWriter
from .heuristics import GreedyScheduler
from .kpis import lateness

def main():
    p = argparse.ArgumentParser(description='Public sample: production scheduling (greedy).')
    p.add_argument('--orders', required=True)
    p.add_argument('--resources', required=True)
    p.add_argument('--out', required=True)
    p.add_argument('--start')
    args = p.parse_args()
    orders = CSVOrdersLoader(args.orders).load_orders()
    resources = CSVResourcesLoader(args.resources).load_resources()
    start = datetime.strptime(args.start, '%Y-%m-%d %H:%M') if args.start else None
    sched = GreedyScheduler(start).build(orders, resources).solve()
    CSVWriter(args.out).write(sched)
    lat = lateness(sched, orders)
    print(json.dumps({'assignments': len(sched), 'avg_lateness_h': sum(max(0.0,v) for v in lat.values())/max(1,len(lat))}, indent=2))

if __name__ == '__main__':
    main()
