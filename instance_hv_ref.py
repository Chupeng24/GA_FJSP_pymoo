import pandas as pd

KHB_data_name_list = ['Kacem1.fjs', 'Kacem2.fjs', 'Kacem3.fjs', 'Kacem4.fjs', 'Kacem5.fjs',]
BR_data_name_list = [f'BrandimarteMk{idx}.fjs'  for idx in range(1, 11)]
DP_data_name_list = [f'DPpaulli{idx}a.fjs' for idx in range(1, 11)]
HU_Rdata_name_list = [f'HurinkRdata{idx}.fjs' for idx in range(1, 67)]
HU_Edata_name_list = [f'HurinkEdata{idx}.fjs' for idx in range(1, 67)]
HU_Vdata_name_list = [f'HurinkVdata{idx}.fjs' for idx in range(1, 67)]

BC_data_path = 'FJSP-benchmarks/Barnes'
KHB_data_path = 'FJSP-benchmarks/Kacem'
BR_data_path = 'FJSP-benchmarks/Brandimarete'
DP_data_path = 'FJSP-benchmarks/DPpaulli'
Be_data_path = 'FJSP-benchmarks/behnke'
HU_Rdata_path = 'FJSP-benchmarks/Hurink_rdata'
HU_Edata_path = 'FJSP-benchmarks/Hurink_edata'
HU_Vdata_path = 'FJSP-benchmarks/Hurink_vdata'
Fat_data_path = 'FJSP-benchmarks/fattahi'

KHB_ins_ref = {
    'Kacem1.fjs': [],
    'Kacem2.fjs': [],
    'Kacem3.fjs': [],
    'Kacem4.fjs': [],
    'Kacem5.fjs': [],
}

BR_ins_ref = {
    'BrandimarteMk1.fjs': [],
    'BrandimarteMk2.fjs': [],
    'BrandimarteMk3.fjs': [],
    'BrandimarteMk4.fjs': [],
    'BrandimarteMk5.fjs': [],
    'BrandimarteMk6.fjs': [],
    'BrandimarteMk7.fjs': [],
    'BrandimarteMk8.fjs': [],
    'BrandimarteMk9.fjs': [],
    'BrandimarteMk10.fjs': [],
}

BC_ins_ref = {
    'mt10c1.fjs': [],
    'mt10cc.fjs': [],
    'mt10x.fjs': [],
    'mt10xx.fjs': [],
    'mt10xxx.fjs': [],
    'mt10xy.fjs': [],
    'mt10xyz.fjs': [],
    'setb4c9.fjs': [],
    'setb4cc.fjs': [],
    'setb4x.fjs': [],
    'setb4xx.fjs': [],
    'setb4xxx.fjs': [],
    'setb4xy.fjs': [],
    'setb4xyz.fjs': [],
    'seti5c12.fjs': [],
    'seti5cc.fjs': [],
    'seti5x.fjs': [],
    'seti5xx.fjs': [],
    'seti5xxx.fjs': [],
    'seti5xy.fjs': [],
    'seti5xyz.fjs': [],
}

DP_ins_ref = {
    'DPpaulli1a.fjs': [],
    'DPpaulli2a.fjs': [],
    'DPpaulli3a.fjs': [],
    'DPpaulli4a.fjs': [],
    'DPpaulli5a.fjs': [],
    'DPpaulli6a.fjs': [],
    'DPpaulli7a.fjs': [],
    'DPpaulli8a.fjs': [],
    'DPpaulli9a.fjs': [],
    'DPpaulli10a.fjs': [],
    'DPpaulli11a.fjs': [],
    'DPpaulli12a.fjs': [],
    'DPpaulli13a.fjs': [],
    'DPpaulli14a.fjs': [],
    'DPpaulli15a.fjs': [],
    'DPpaulli16a.fjs': [],
    'DPpaulli17a.fjs': [],
    'DPpaulli18a.fjs': [],
}

HU_Rdata_ins_ref = {
    'abz5.fjs': [],
    'abz6.fjs': [],
    'abz7.fjs': [],
    'abz8.fjs': [],
    'abz9.fjs': [],
    'car1.fjs': [],
    'car2.fjs': [],
    'car3.fjs': [],
    'car4.fjs': [],
    'car5.fjs': [],
    'car6.fjs': [],
    'car7.fjs': [],
    'car8.fjs': [],
    'la01.fjs': [],
    'la02.fjs': [],
    'la03.fjs': [],
    'la04.fjs': [],
    'la05.fjs': [],
    'la06.fjs': [],
    'la07.fjs': [],
    'la08.fjs': [],
    'la09.fjs': [],
    'la10.fjs': [],
    'la11.fjs': [],
    'la12.fjs': [],
    'la13.fjs': [],
    'la14.fjs': [],
    'la15.fjs': [],
    'la16.fjs': [],
    'la17.fjs': [],
    'la18.fjs': [],
    'la19.fjs': [],
    'la20.fjs': [],
    'la21.fjs': [],
    'la22.fjs': [],
    'la23.fjs': [],
    'la24.fjs': [],
    'la25.fjs': [],
    'la26.fjs': [],
    'la27.fjs': [],
    'la28.fjs': [],
    'la29.fjs': [],
    'la30.fjs': [],
    'la31.fjs': [],
    'la32.fjs': [],
    'la33.fjs': [],
    'la34.fjs': [],
    'la35.fjs': [],
    'la36.fjs': [],
    'la37.fjs': [],
    'la38.fjs': [],
    'la39.fjs': [],
    'la40.fjs': [],
    'mt06.fjs': [],
    'mt10.fjs': [],
    'mt20.fjs': [],
    'orb1.fjs': [],
    'orb2.fjs': [],
    'orb3.fjs': [],
    'orb4.fjs': [],
    'orb5.fjs': [],
    'orb6.fjs': [],
    'orb7.fjs': [],
    'orb8.fjs': [],
    'orb9.fjs': [],
    'orb10.fjs': [],
}

HU_Edata_ins_ref = {
    'abz5.fjs': [],
    'abz6.fjs': [],
    'abz7.fjs': [],
    'abz8.fjs': [],
    'abz9.fjs': [],
    'car1.fjs': [],
    'car2.fjs': [],
    'car3.fjs': [],
    'car4.fjs': [],
    'car5.fjs': [],
    'car6.fjs': [],
    'car7.fjs': [],
    'car8.fjs': [],
    'la01.fjs': [],
    'la02.fjs': [],
    'la03.fjs': [],
    'la04.fjs': [],
    'la05.fjs': [],
    'la06.fjs': [],
    'la07.fjs': [],
    'la08.fjs': [],
    'la09.fjs': [],
    'la10.fjs': [],
    'la11.fjs': [],
    'la12.fjs': [],
    'la13.fjs': [],
    'la14.fjs': [],
    'la15.fjs': [],
    'la16.fjs': [],
    'la17.fjs': [],
    'la18.fjs': [],
    'la19.fjs': [],
    'la20.fjs': [],
    'la21.fjs': [],
    'la22.fjs': [],
    'la23.fjs': [],
    'la24.fjs': [],
    'la25.fjs': [],
    'la26.fjs': [],
    'la27.fjs': [],
    'la28.fjs': [],
    'la29.fjs': [],
    'la30.fjs': [],
    'la31.fjs': [],
    'la32.fjs': [],
    'la33.fjs': [],
    'la34.fjs': [],
    'la35.fjs': [],
    'la36.fjs': [],
    'la37.fjs': [],
    'la38.fjs': [],
    'la39.fjs': [],
    'la40.fjs': [],
    'mt06.fjs': [],
    'mt10.fjs': [],
    'mt20.fjs': [],
    'orb1.fjs': [],
    'orb2.fjs': [],
    'orb3.fjs': [],
    'orb4.fjs': [],
    'orb5.fjs': [],
    'orb6.fjs': [],
    'orb7.fjs': [],
    'orb8.fjs': [],
    'orb9.fjs': [],
    'orb10.fjs': [],
}

HU_Vdata_ins_ref = {
    'abz5.fjs': [],
    'abz6.fjs': [],
    'abz7.fjs': [],
    'abz8.fjs': [],
    'abz9.fjs': [],
    'car1.fjs': [],
    'car2.fjs': [],
    'car3.fjs': [],
    'car4.fjs': [],
    'car5.fjs': [],
    'car6.fjs': [],
    'car7.fjs': [],
    'car8.fjs': [],
    'la01.fjs': [],
    'la02.fjs': [],
    'la03.fjs': [],
    'la04.fjs': [],
    'la05.fjs': [],
    'la06.fjs': [],
    'la07.fjs': [],
    'la08.fjs': [],
    'la09.fjs': [],
    'la10.fjs': [],
    'la11.fjs': [],
    'la12.fjs': [],
    'la13.fjs': [],
    'la14.fjs': [],
    'la15.fjs': [],
    'la16.fjs': [],
    'la17.fjs': [],
    'la18.fjs': [],
    'la19.fjs': [],
    'la20.fjs': [],
    'la21.fjs': [],
    'la22.fjs': [],
    'la23.fjs': [],
    'la24.fjs': [],
    'la25.fjs': [],
    'la26.fjs': [],
    'la27.fjs': [],
    'la28.fjs': [],
    'la29.fjs': [],
    'la30.fjs': [],
    'la31.fjs': [],
    'la32.fjs': [],
    'la33.fjs': [],
    'la34.fjs': [],
    'la35.fjs': [],
    'la36.fjs': [],
    'la37.fjs': [],
    'la38.fjs': [],
    'la39.fjs': [],
    'la40.fjs': [],
    'mt06.fjs': [],
    'mt10.fjs': [],
    'mt20.fjs': [],
    'orb1.fjs': [],
    'orb2.fjs': [],
    'orb3.fjs': [],
    'orb4.fjs': [],
    'orb5.fjs': [],
    'orb6.fjs': [],
    'orb7.fjs': [],
    'orb8.fjs': [],
    'orb9.fjs': [],
    'orb10.fjs': [],
}

ins_set_ref = dict()
ins_set_ref['FJSP-benchmarks/Kacem'] = KHB_ins_ref
ins_set_ref['FJSP-benchmarks/Brandimarete'] =  BR_ins_ref
ins_set_ref['FJSP-benchmarks/Barnes'] = BC_ins_ref
ins_set_ref['FJSP-benchmarks/DPpaulli'] = DP_ins_ref
ins_set_ref['FJSP-benchmarks/Hurink_rdata'] = HU_Rdata_ins_ref
ins_set_ref['FJSP-benchmarks/Hurink_edata'] = HU_Edata_ins_ref
ins_set_ref['FJSP-benchmarks/Hurink_vdata'] = HU_Vdata_ins_ref