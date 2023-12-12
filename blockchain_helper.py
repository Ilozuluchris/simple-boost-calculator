import os

from web3 import Web3

w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{os.environ["INFURA_PROJECT_ID"]}'))
if not w3.is_connected(show_traceback=True):
    print("w3 not connected")
    exit()

vault_abi = '[{"inputs":[{"internalType":"address","name":"_prismaCore","type":"address"},{"internalType":"contract IPrismaToken","name":"_token","type":"address"},{"internalType":"contract ITokenLocker","name":"_locker","type":"address"},{"internalType":"contract IIncentiveVoting","name":"_voter","type":"address"},{"internalType":"address","name":"_stabilityPool","type":"address"},{"internalType":"address","name":"_manager","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"boostCalculator","type":"address"}],"name":"BoostCalculatorSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"boostDelegate","type":"address"},{"indexed":false,"internalType":"bool","name":"isEnabled","type":"bool"},{"indexed":false,"internalType":"uint256","name":"feePct","type":"uint256"},{"indexed":false,"internalType":"address","name":"callback","type":"address"}],"name":"BoostDelegationSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"emissionScheduler","type":"address"}],"name":"EmissionScheduleSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"receiver","type":"address"},{"indexed":false,"internalType":"uint256","name":"increasedAmount","type":"uint256"}],"name":"IncreasedAllocation","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"receiver","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"}],"name":"NewReceiverRegistered","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"bool","name":"isActive","type":"bool"}],"name":"ReceiverIsActiveStatusModified","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"increasedAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"unallocatedTotal","type":"uint256"}],"name":"UnallocatedSupplyIncreased","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"reducedAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"unallocatedTotal","type":"uint256"}],"name":"UnallocatedSupplyReduced","type":"event"},{"inputs":[],"name":"PRISMA_CORE","outputs":[{"internalType":"contract IPrismaCore","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"allocateNewEmissions","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"allocated","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"address","name":"boostDelegate","type":"address"},{"internalType":"contract IRewards[]","name":"rewardContracts","type":"address[]"},{"internalType":"uint256","name":"maxFeePct","type":"uint256"}],"name":"batchClaimRewards","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"boostCalculator","outputs":[{"internalType":"contract IBoostCalculator","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"boostDelegation","outputs":[{"internalType":"bool","name":"isEnabled","type":"bool"},{"internalType":"uint16","name":"feePct","type":"uint16"},{"internalType":"contract IBoostDelegate","name":"callback","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"}],"name":"claimBoostDelegationFees","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"claimant","type":"address"}],"name":"claimableBoostDelegationFees","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"receiver","type":"address"},{"internalType":"address","name":"boostDelegate","type":"address"},{"internalType":"contract IRewards","name":"rewardContract","type":"address"}],"name":"claimableRewardAfterBoost","outputs":[{"internalType":"uint256","name":"adjustedAmount","type":"uint256"},{"internalType":"uint256","name":"feeToDelegate","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"deploymentManager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"emissionSchedule","outputs":[{"internalType":"contract IEmissionSchedule","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"claimant","type":"address"}],"name":"getClaimableWithBoost","outputs":[{"internalType":"uint256","name":"maxBoosted","type":"uint256"},{"internalType":"uint256","name":"boosted","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getWeek","outputs":[{"internalType":"uint256","name":"week","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"guardian","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"idToReceiver","outputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bool","name":"isActive","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"increaseUnallocatedSupply","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"lockWeeks","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"locker","outputs":[{"internalType":"contract ITokenLocker","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"prismaToken","outputs":[{"internalType":"contract IPrismaToken","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"receiverUpdatedWeek","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"count","type":"uint256"}],"name":"registerReceiver","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IBoostCalculator","name":"_boostCalculator","type":"address"}],"name":"setBoostCalculator","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"isEnabled","type":"bool"},{"internalType":"uint256","name":"feePct","type":"uint256"},{"internalType":"address","name":"callback","type":"address"}],"name":"setBoostDelegationParams","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IEmissionSchedule","name":"_emissionSchedule","type":"address"}],"name":"setEmissionSchedule","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IEmissionSchedule","name":"_emissionSchedule","type":"address"},{"internalType":"contract IBoostCalculator","name":"_boostCalculator","type":"address"},{"internalType":"uint256","name":"totalSupply","type":"uint256"},{"internalType":"uint64","name":"initialLockWeeks","type":"uint64"},{"internalType":"uint128[]","name":"_fixedInitialAmounts","type":"uint128[]"},{"components":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct PrismaVault.InitialAllowance[]","name":"initialAllowances","type":"tuple[]"}],"name":"setInitialParameters","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"bool","name":"isActive","type":"bool"}],"name":"setReceiverIsActive","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalUpdateWeek","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"claimant","type":"address"},{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferAllocatedTokens","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token","type":"address"},{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferTokens","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unallocatedTotal","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"voter","outputs":[{"internalType":"contract IIncentiveVoting","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"weeklyEmissions","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"view","type":"function"}]'

vault_contract_address = "0x06bDF212C290473dCACea9793890C5024c7Eb02c"
vault_contract = w3.eth.contract(address=vault_contract_address, abi=vault_abi)

boost_contract_address = "0x31ae4cbfaFB007a908F348Cf95Ce4b535D5A8fa3"
boost_contract_abi = '[{"inputs":[{"internalType":"address","name":"_prismaCore","type":"address"},{"internalType":"contract ITokenLocker","name":"_locker","type":"address"},{"internalType":"uint256","name":"_graceWeeks","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"MAX_BOOST_GRACE_WEEKS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"previousAmount","type":"uint256"},{"internalType":"uint256","name":"totalWeeklyEmissions","type":"uint256"}],"name":"getBoostedAmount","outputs":[{"internalType":"uint256","name":"adjustedAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"previousAmount","type":"uint256"},{"internalType":"uint256","name":"totalWeeklyEmissions","type":"uint256"}],"name":"getBoostedAmountWrite","outputs":[{"internalType":"uint256","name":"adjustedAmount","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"claimant","type":"address"},{"internalType":"uint256","name":"previousAmount","type":"uint256"},{"internalType":"uint256","name":"totalWeeklyEmissions","type":"uint256"}],"name":"getClaimableWithBoost","outputs":[{"internalType":"uint256","name":"maxBoosted","type":"uint256"},{"internalType":"uint256","name":"boosted","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getWeek","outputs":[{"internalType":"uint256","name":"week","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"locker","outputs":[{"internalType":"contract ITokenLocker","name":"","type":"address"}],"stateMutability":"view","type":"function"}]'
boost_contract = w3.eth.contract(address=boost_contract_address, abi=boost_contract_abi)


token_locker_address = "0x3f78544364c3eCcDCe4d9C89a630AEa26122829d"
token_locker_abi = '[{"inputs":[{"internalType":"address","name":"_prismaCore","type":"address"},{"internalType":"contract IPrismaToken","name":"_token","type":"address"},{"internalType":"contract IIncentiveVoting","name":"_voter","type":"address"},{"internalType":"address","name":"_manager","type":"address"},{"internalType":"uint256","name":"_lockToTokenRatio","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_weeks","type":"uint256"}],"name":"LockCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_weeks","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newWeeks","type":"uint256"}],"name":"LockExtended","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"components":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"weeksToUnlock","type":"uint256"}],"indexed":false,"internalType":"struct TokenLocker.LockData[]","name":"newLocks","type":"tuple[]"}],"name":"LocksCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"components":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"currentWeeks","type":"uint256"},{"internalType":"uint256","name":"newWeeks","type":"uint256"}],"indexed":false,"internalType":"struct TokenLocker.ExtendLockData[]","name":"locks","type":"tuple[]"}],"name":"LocksExtended","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"LocksFrozen","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"LocksUnfrozen","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"withdrawn","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"penalty","type":"uint256"}],"name":"LocksWithdrawn","type":"event"},{"inputs":[],"name":"MAX_LOCK_WEEKS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PRISMA_CORE","outputs":[{"internalType":"contract IPrismaCore","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"allowPenaltyWithdrawAfter","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"deploymentManager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_weeks","type":"uint256"},{"internalType":"uint256","name":"_newWeeks","type":"uint256"}],"name":"extendLock","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"currentWeeks","type":"uint256"},{"internalType":"uint256","name":"newWeeks","type":"uint256"}],"internalType":"struct TokenLocker.ExtendLockData[]","name":"newExtendLocks","type":"tuple[]"}],"name":"extendMany","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"freeze","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"minWeeks","type":"uint256"}],"name":"getAccountActiveLocks","outputs":[{"components":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"weeksToUnlock","type":"uint256"}],"internalType":"struct TokenLocker.LockData[]","name":"lockData","type":"tuple[]"},{"internalType":"uint256","name":"frozenAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getAccountBalances","outputs":[{"internalType":"uint256","name":"locked","type":"uint256"},{"internalType":"uint256","name":"unlocked","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getAccountWeight","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"week","type":"uint256"}],"name":"getAccountWeightAt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getAccountWeightWrite","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getTotalWeight","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"week","type":"uint256"}],"name":"getTotalWeightAt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalWeightWrite","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getWeek","outputs":[{"internalType":"uint256","name":"week","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amountToWithdraw","type":"uint256"}],"name":"getWithdrawWithPenaltyAmounts","outputs":[{"internalType":"uint256","name":"amountWithdrawn","type":"uint256"},{"internalType":"uint256","name":"penaltyAmountPaid","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"guardian","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"incentiveVoter","outputs":[{"internalType":"contract IIncentiveVoting","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_weeks","type":"uint256"}],"name":"lock","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_account","type":"address"},{"components":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"weeksToUnlock","type":"uint256"}],"internalType":"struct TokenLocker.LockData[]","name":"newLocks","type":"tuple[]"}],"name":"lockMany","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"lockToTokenRatio","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lockToken","outputs":[{"internalType":"contract IPrismaToken","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"penaltyWithdrawalsEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"prismaCore","outputs":[{"internalType":"contract IPrismaCore","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_timestamp","type":"uint256"}],"name":"setAllowPenaltyWithdrawAfter","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_enabled","type":"bool"}],"name":"setPenaltyWithdrawalsEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalDecayRate","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalUpdatedWeek","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"keepIncentivesVote","type":"bool"}],"name":"unfreeze","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_weeks","type":"uint256"}],"name":"withdrawExpiredLocks","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountToWithdraw","type":"uint256"}],"name":"withdrawWithPenalty","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"}]'
token_locker_contract = w3.eth.contract(address=token_locker_address, abi=token_locker_abi)


vault_contract_current_week = vault_contract.functions.getWeek().call()
boost_contract_current_week = boost_contract.functions.getWeek().call()
token_locker_current_week = token_locker_contract.functions.getWeek().call()

if vault_contract_current_week != boost_contract_current_week != token_locker_current_week:
    exit("Contracts  are not correct")


def get_current_week():
    current_week = vault_contract.functions.getWeek().call()
    return current_week

def get_account_weight(claimant, week):
    """
    Get an accounts weight at week
    :param claimant: Address to claim
    :param week: Int used to get account weight at week, cant be in the future?
    :return: Int weight of a certain account
    """


    return int(token_locker_contract.functions.getAccountWeightAt(claimant, week).call())

def get_total_weight(week):
    """
    Get total weight at a certain week. Week can't be in the future
    :param week: Int
    :return: Int total weight
    """
    return int(token_locker_contract.functions.getTotalWeightAt(week).call())

def calculate_emissions_for_week(total_prisma, week):
    high_emission_period = 4
    prisma_released_high_per_week = 9000000 / high_emission_period

    if week <= high_emission_period:
        return prisma_released_high_per_week

    week = week - 4
    if week <= 4:
        return 2250000
    elif week <= 13:
        return total_prisma * 0.012
    elif week <= 26:
        return total_prisma * 0.01
    elif week <= 39:
        return total_prisma * 0.009
    elif week <= 52:
        return total_prisma * 0.008
    elif week <= 52 * 2:
        return total_prisma * 0.007
    elif week <= 52 * 3:
        return total_prisma * 0.006
    else:
        return total_prisma * 0.005


def calculate_remaining_prisma(total_prisma_available, weeks_to_calculate):
    remaining_prisma = total_prisma_available
    emissions = {}

    for week in range(1, weeks_to_calculate + 1):
        emissions[week] = calculate_emissions_for_week(remaining_prisma, week)
        remaining_prisma -= emissions[week]

    return emissions, remaining_prisma

def get_emission_for_week(week_to_find):
    # total_prisma_available = 186000000
    total_prisma_available = 300000000000000000000000000

    weeks_to_calculate = 156 + 4  # Three years of emissions +  4 weeks of high prisma reward

    emissions_data, remaining_prisma = calculate_remaining_prisma(total_prisma_available, weeks_to_calculate)

    if week_to_find <= weeks_to_calculate:
        if week_to_find in emissions_data:
            print(f"Emissions for week {week_to_find}: {emissions_data[week_to_find]}")
            return emissions_data[week_to_find]
    else:
        new_emission = 0
        for week in range(weeks_to_calculate + 1, week_to_find + 1):
            new_emission = calculate_emissions_for_week(remaining_prisma, week)
            remaining_prisma -= new_emission
        return new_emission

def get_total_emissions(week, current_week):
    if week <= current_week:
        return vault_contract.functions.weeklyEmissions(week).call()
    return get_emission_for_week(week)


def boost_calc(claimant, weeks_in_future):
    current_week = get_current_week()
    week = current_week + weeks_in_future
    total_emissions = get_total_emissions(week, current_week)

    return boost_calc_from_contract(claimant, 0, total_emissions, week, current_week)

def boost_calc_from_contract(claimant, previous_amount, total_weekly_emissions, week, current_week):
    max_boost_week = boost_contract.functions.MAX_BOOST_GRACE_WEEKS().call()

    if week < max_boost_week:
        remaining_amount = total_weekly_emissions - previous_amount
        return remaining_amount, remaining_amount

    current_week = current_week - 1

    account_weight = get_account_weight(claimant, current_week)
    total_weight = get_total_weight(current_week)

    if total_weight == 0: total_weight = 1
    pct = (1e9 * account_weight) / total_weight

    if pct == 0: return 0, 0

    max_boostable = (total_weekly_emissions * pct) / 1e9
    full_decay = max_boostable * 2

    max_boosted = 0 if previous_amount >= max_boostable else max_boostable - previous_amount
    boosted = 0 if previous_amount >= full_decay else full_decay - max_boostable

    return max_boosted, boosted
