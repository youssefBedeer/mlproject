@dataclass 
class TransformerConfig:
    preprocessor_path = os.path.join("artifacts","preprocessor.pkl")

class Transformer:
    def __init__(self):
        self.transformer_config = TransformerConfig() 

    def get_preprocessor(self):
        num_cols 
        cat_cols

        num_pipeleine([steps=[
            ("imputer",SimpleImputer(strategy="median")),
            ("Scaler",StandardScaler())
        ]])

        cat_pipeleine([steps=[
            ("imputer",SimpleImputer(strategy="median")),
            ("Scaler",StandardScaler())
        ]])

        preprocessor = Pipeline(
            ("num_pipeline", num_pipeline, num_cols),
            ("cat_pipeline", cat_pipeline, cat_cols)
        )

        return preprocessor


    def intiate_preprocessor(self, train_data, test_data):
        X_train = train_data[:, :-1]
        X_test = test_data[:, :-1]
        y_train= train_data[:, -1]
        y_test = test_data[:, -1]

        preprocessor_obj = get_preprocessor()
        input_train = preprocessor_obj.fit_transform(X_train)
        input_test  = preprocessor_obj.transform(X_test)

        preprocessed_train= np.c_([input_train, y_train])
        preprocessed_test = np.c_([input_test, y_test])



        return (
            preprocessed_train,
            preprocessed_test,
            self.transformer_config
        )
