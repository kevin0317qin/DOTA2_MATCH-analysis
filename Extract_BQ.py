import google.auth
from google.cloud import bigquery
from google.cloud import bigquery_storage_v1beta1
from Query import Sql
import collections

# Explicitly create a credentials object. This allows you to use the same
# credentials for both the BigQuery and BigQuery Storage clients, avoiding
# unnecessary API calls to fetch duplicate authentication tokens.
credentials, your_project_id = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

# Make clients.
bqclient = bigquery.Client(
    credentials=credentials,
    project=your_project_id,
)
bqstorageclient = bigquery_storage_v1beta1.BigQueryStorageClient(
    credentials=credentials
)
def BQ_GET_WINRATE():


    query_string = Sql.win_rate
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    object = []
    rate = []
    for index, row in dataframe.iterrows():
        rate.append(row['RATE'])
        object.append(row['localized_name'])

    query_string = Sql.win_avg

    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    for index, row in dataframe.iterrows():
        avg = row['AVG']

    return object, rate, avg

def BQ_GET_WINRATE_TOP30():


    query_string = Sql.win_rate_top30
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    object = []
    rate = []
    for index, row in dataframe.iterrows():
        rate.append(row['RATE'])
        object.append(row['localized_name'])

    query_string = Sql.win_avg

    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    for index, row in dataframe.iterrows():
        avg = row['AVG']

    return object, rate, avg

def BQ_GET_WINRATE_BOTTOM15():


    query_string = Sql.win_rate_bottom15
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    object = []
    rate = []
    for index, row in dataframe.iterrows():
        rate.append(row['RATE'])
        object.append(row['localized_name'])

    query_string = Sql.win_avg

    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    for index, row in dataframe.iterrows():
        avg = row['AVG']

    return object, rate, avg



def BQ_GET_USERATE():
    query_string = Sql.use_rate_30
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    object = []
    rate = []
    for index, row in dataframe.iterrows():
        rate.append(row['use_rate'])
        object.append(row['localized_name'])

    query_string = Sql.use_avg

    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    for index, row in dataframe.iterrows():
        avg = row['AVG']

    return object, rate, avg

def BQ_GET_USERATE_30():
    query_string = Sql.use_rate_30
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    object = []
    rate = []
    for index, row in dataframe.iterrows():
        rate.append(row['use_rate'])
        object.append(row['localized_name'])

    query_string = Sql.use_avg

    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    for index, row in dataframe.iterrows():
        avg = row['AVG']

    return object, rate, avg

def BQ_GET_ADVANTAGES():
    query_string = Sql.gold_xp_min
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    minute = []
    gold = []
    xp = []
    for index, row in dataframe.iterrows():
        if (row['minute'] not in minute):
            minute.append(row['minute'])
        if (row['gold_or_xp'] == 0):
            gold.append(row['value'])
        else:
            xp.append(row['value'])

    return minute, gold, xp

def BQ_GET_A1_USERATE():
    query_string = Sql.analytic_temp + Sql.analytic_1_get_useRate
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    rate =[]
    id = []
    for index, row in dataframe.iterrows():
        rate.append(row['use_rate'])
        id.append(row['hero_id'])

    return id, rate

def BQ_GET_A1_BANRATE():
    query_string = Sql.analytic_1_get_avgBan

    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    for index, row in dataframe.iterrows():
        avg = row['avg_ban']

    query_string = Sql.analytic_temp + Sql.analytic_1_get_banRate
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    rate = []
    id = []
    for index, row in dataframe.iterrows():
        rate.append(row['ban_rate'])
        id.append(row['hero_id'])

    return id, rate, avg

def BQ_GET_A1_GOODDATA():
    query_string = Sql.analytic_temp + Sql.analytic_1_get_good_data
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    id = []
    val = []
    for index, row in dataframe.iterrows():
        val.append(row['good_val'])
        id.append(row['hero_id'])

    return id, val

def BQ_GET_A1_OPPNENTHEADACHE():
    query_string = Sql.analytic_temp + Sql.analytic_1_get_opponent_headache
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    id = []
    val = []
    for index, row in dataframe.iterrows():
        val.append(row['headache_val'])
        id.append(row['hero_id'])

    return id, val

def BQ_GET_USERATEANDFACEVALUE():
    query_string = Sql.analytic_2_useRate_faceValue
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    name = []
    rate = []
    face = []
    for index, row in dataframe.iterrows():
        name.append(row['localized_name'])
        rate.append(row['use_rate'])
        face.append(row['face_value'])

    return name, rate, face

def BQ_GET_DISTRIBUTION_BFURY():
    query_string = Sql.analytic_3_rate
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    dis = []
    for index, row in dataframe.iterrows():
        dis.append(row['val'])

    return dis

def BQ_GET_WIN_RATE_BFURY():
    query_string = Sql.analytic_3_win_rate_bf
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    rate = []
    for index, row in dataframe.iterrows():
        rate.append(row['RATE'])

    return rate
def BQ_GET_TIME_WITHBFURY():
    query_string = Sql.analytic_3_time_with_bf
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    time = []

    for index, row in dataframe.iterrows():
        time.append(row['t1'])
        time.append(row['t2'])
        time.append(row['t3'])
        time.append(row['t4'])
        time.append(row['t5'])
        avg = row['avg']

    return time, avg

def BQ_GET_TIME_WITHOUTBFURY():
    query_string = Sql.analytic_3_time_without_bf
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    time = []
    for index, row in dataframe.iterrows():
        time.append(row['t1'])
        time.append(row['t2'])
        time.append(row['t3'])
        time.append(row['t4'])
        time.append(row['t5'])
        avg = row['avg']

    return time, avg

def BQ_GET_MINUTE():
    query_string = Sql.analytic_3_minute
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    minute = []
    all = []
    win = []
    for index, row in dataframe.iterrows():
        minute.append(row['minute'])
        all.append(row['a'])
        win.append(row['win'])
    return minute, all, win

def BQ_GET_TEAM():
    query_string = Sql.analytic_3_team
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    team_gold = collections.defaultdict(list)
    team_xp = collections.defaultdict(list)
    id = []
    gold = []
    xp = []
    for index, row in dataframe.iterrows():
        if row['match_id'] not in id:
            if len(id) > 0:
                # team_gold.update({id.pop(), gold})
                t_gold = gold.copy()
                team_gold[id[0]] = t_gold
                # team_xp.update({id.pop(), xp})
                t_xp = xp.copy()
                team_xp[id[0]] = t_xp
                id.clear()
                gold.clear()
                xp.clear()
            else:
                id.append(row['match_id'])

        if row['gold_or_xp'] == 0:
            gold.append(row['value'])
        elif row['gold_or_xp'] == 1:
            xp.append(row['value'])

    return team_gold, team_xp


def BQ_GET_EQUIP():
    query_string = Sql.analytic_3_equipment
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )

    items = []
    val = []
    for index, row in dataframe.iterrows():
        items.append(row['key'])
        val.append(row['v'])

    return items, val

def BQ_GET_EFFECT():
    query_string = Sql.analytic_4_effect
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    id = []
    gold = []
    xp = []
    radiant = []

    for index, row in dataframe.iterrows():
        if row['match_id'] not in id:
            id.append(row['match_id'])
            radiant.append(row['radiant_win'])

        if row['gold_or_xp'] == 0:
            gold.append(row['value'])
        else:
            xp.append(row['value'])

    return id, gold, xp, radiant

def BQ_GET_COUNT():
    query_string = Sql.analytic_4_count
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    count = {}
    for index, row in dataframe.iterrows():
        count[row['type']] = row['value']

    return count

def BQ_GET_GOLD():
    query_string = Sql.analytic_4_gold
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    lose = {}
    for index, row in dataframe.iterrows():
        lose[row['t']] = row['val']

    return lose

def BQ_GET_XP():
    query_string = Sql.analytic_4_xp
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    lose = {}

    for index, row in dataframe.iterrows():
        lose[row['t']] = row['val']

    return lose

def BQ_GET_D():
    query_string = Sql.analytic_4_d
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    val = {}

    for index, row in dataframe.iterrows():
        val[row['type']] = row['v']
    return val

def BQ_GET_HERO():
    query_string = Sql.analytic_4_hero
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    id = []
    val = []
    for index, row in dataframe.iterrows():
        id.append(row['hero_id'])
        val.append(row['value'])

    return id, val

def BQ_GET_TOP1():
    query_string = Sql.analytic_top1
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    for index, row in dataframe.iterrows():
        normal = row['normal']
        hard = row['hard']
        veryhard = row['veryhard']
    return normal, hard, veryhard

def BQ_GET_TOP2():
    query_string = Sql.analytic_top2
    dataframe = (
        bqclient.query(query_string)
            .result()
            .to_dataframe(bqstorage_client=bqstorageclient)
    )
    for index, row in dataframe.iterrows():
        kill = row['kill']
        death = row['death']
        assists = row['assists']
    return kill, death, assists