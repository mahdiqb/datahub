import numpy as np
import datahub_core.generators as gen
import datahub_core.data as data

def run():
    df = gen.generate(
        props={
            'region': gen.choice(
                data=['EMEA', 'LATAM', 'NAM', 'APAC'],
                weights=[0.1, 0.1, 0.3, 0.5]),
            'firmAccount': gen.normal_sampler(
                data=['fa1', 'fa2', 'fa3', 'fa4', 'fa5', 'fa6']),
            "country": gen.country_codes(region_field='region'),
            "client_type": gen.choice(data=data.client_types()),
            "client_name": gen.company_namer(
                field='client_type',
                field_type='client_type',
                countrycode_field='country'
            )},
        count=50,
        randomstate=np.random.RandomState(13031981)
    ).to_dataframe()

    print(df)


run()
