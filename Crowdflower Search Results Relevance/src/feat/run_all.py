import os

#################
## Preprocesss ##
#################
#### preprocess data
cmd = "python src/feat/preprocess.py"
os.system(cmd)

# #### generate kfold
# cmd = "python ./gen_kfold.py"
# os.system(cmd)

#######################
## Generate features ##
#######################
#### query id
cmd = "python src/feat/genFeat_id_feat.py"
os.system(cmd)

#### counting feat
cmd = "python src/feat/genFeat_counting_feat.py"
os.system(cmd)

#### distance feat
cmd = "python src/feat/genFeat_distance_feat.py"
os.system(cmd)

#### basic tfidf
cmd = "python src/feat/genFeat_basic_tfidf_feat.py"
os.system(cmd)

#### cooccurrence tfidf
cmd = "python src/feat/genFeat_cooccurrence_tfidf_feat.py"
os.system(cmd)


#####################
## Combine Feature ##
#####################
#### combine feat
cmd = "python src/feat/combine_feat_[LSA_and_stats_feat_Jun09]_[Low].py"
os.system(cmd)

#### combine feat
cmd = "python src/feat/combine_feat_[LSA_svd150_and_Jaccard_coef_Jun14]_[Low].py"
os.system(cmd)

#### combine feat
cmd = "python src/feat/combine_feat_[svd100_and_bow_Jun23]_[Low].py"
os.system(cmd)

#### combine feat
cmd = "python src/feat/combine_feat_[svd100_and_bow_Jun27]_[High].py"
os.system(cmd)