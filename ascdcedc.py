import pandas as pd
main_df = pd.DataFrame()
main_df.columns = ["Tarih", "Yeşillik", "Karpuz", "Nuri", "Diger_Giderler", "Kasa_4", "Kasa_5", "Şube"]

main_df.loc[len(main_df.index)] = [20, 7, 5,1,1,1,1,1]
print(main_df)