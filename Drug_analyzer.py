class DrugAnalyzer:
    # TODO: Part 1 - Add method(s) necessary to fulfill the requirements.

    def __init__(self,data=[]):
        self.data = data 
        pass

    def __add__(self,list):

        if len(list) == 4:
            temp = self.data.copy()
            temp.append(list)
            return DrugAnalyzer(temp)
        else:
            raise ValueError("Error, length of list does not match")
        
    def verify_series(
        self,
        series_id: str,
        act_subst_wgt: float,
        act_subst_rate: float,
        allowed_imp: float,
    ) -> bool:

        pesoT = susT = impT = pill = 0
        for id in self.data:
            if series_id in id[0]:
                pesoT += id[1]
                susT += id[2]
                impT += id[3]
                pill += 1 
        
        if pesoT == 0:
            raise ValueError("The pill was not found")
        
        Crrctwght = False
        Impurity = False

        final_weight = pill * act_subst_wgt
        Correct_percentage = final_weight * act_subst_rate
        pesominimo = (final_weight - Correct_percentage)
        pesomaximo = (final_weight + Correct_percentage)

        imp_accepted = pesoT * allowed_imp

        if impT <= imp_accepted:
            Impurity = True

        if pesominimo < susT and susT < pesomaximo:
            Crrctwght = True
        
        if Impurity and Crrctwght:
            return True
        else:
            return False