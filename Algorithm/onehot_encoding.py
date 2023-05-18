# onehot encoding
def ohe_encode(X_):
   
   ohe = OneHotEncoder()
   X_cat = X_.select_dtypes('category')
   ohe.fit(X_cat)

   codes = ohe.transform(X_cat).toarray()
   feature_names = ohe.get_feature_names_out(X_cat.columns)


   X_ = pd.concat([X_.select_dtypes(exclude='category'),
                  pd.DataFrame(codes, columns=feature_names).astype(int)], axis = 1)

   return X_, ohe


ohe.transform(X_)
