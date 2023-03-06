import os
import concurrent.futures

potentials = ["0x5CA42204cDaa70d5c773946e69dE942b85CA6706", 
              "0x073D31b72E5444E6F00e24D31F66f100dEE40E74", 
              "0xdFd9e2A17596caD6295EcFfDa42D9B6F63F7B5d5",
               "0xc53708664b99DF348dd27C3Ac0759d2DA9c40462",
               "0x6c1eFbEd2F57dd486Ec091dFfd08eE5235A570b1",
               "0x0F1cBEd8EFa0E012AdbCCB1638D0aB0147D5Ac00",
               "0x1D1eb8E8293222e1a29d2C0E4cE6C0Acfd89AaaC",
               "0x9c4a515cd72D27A4710571Aca94858a53D9278D5"
            ]

#
command = "myth analyze -a {} --rpc bsc-dataseed1.binance.org:443 --rpctls True --infura-id ba06a11d8b764e8192810e25ee8befb5"


for item in potentials:
    filename = f'{item}.txt'
    os.system(f'myth analyze -a {item} --rpc bsc-dataseed1.binance.org:443 --rpctls True --infura-id ba06a11d8b764e8192810e25ee8befb5 > {filename}')

    while not os.path.exists(filename):
        pass

    print(f'Processed contract: {item}')

# def process_item(item):
#     filename = f'{item}.txt'
#     os.system(f'myth analyze -a {item} --rpc bsc-dataseed1.binance.org:443 --rpctls True --infura-id ba06a11d8b764e8192810e25ee8befb5 > {filename}')

#     while not os.path.exists(filename):
#         pass

#     print(f'Processed contract: {item}')


# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#     futures = []
#     for item in potentials:
#         futures.append(executor.submit(process_item, item))

#     concurrent.futures.wait(futures)

