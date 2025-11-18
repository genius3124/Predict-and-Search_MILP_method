from ecole.instance import SetCoverGenerator, CombinatorialAuctionGenerator

TaskName="CA"


if TaskName=="SC":
    generator = SetCoverGenerator(n_rows=100, n_cols=200, density=0.1)
elif TaskName=="CA":
    generator = CombinatorialAuctionGenerator(n_items=100, n_bids=200)

for i in range(50):
    instance = next(generator)
    instance.write_problem(f"instance/train/{TaskName}/{i:04}.lp")
