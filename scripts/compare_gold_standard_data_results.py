import sys
import csv

def convert_datafile_to_dict(datafilename):

    urim_topic_ratings = {}

    with open(gold_standard_file) as tsvfile:

        reader = csv.DictReader(delimiter='\t')

        for row in reader:

            urim = row['URI']
            topic_rating = row['label']
            ontopic = False

            if topic_rating == "1":
                ontopic = True

            urim_topic_ratings[urim] = ontopic

    return urim_topic_ratings

if __name__ == '__main__':

    gold_standard_file = sys.argv[1]
    off_topic_output_file = sys.argv[2]

    gold_standard_urim_topic_ratings = \
        convert_datafile_to_dict(gold_standard_file)
    off_topic_output_topic_ratings = \
        convert_datafile_to_dict(off_topic_output_file)

    true_positives = []
    false_positives = []
    true_negatives = []
    false_negatives = []

    for urim in gold_standard_urim_topic_ratings:

        if gold_standard_urim_topic_ratings[urim] == True \
            and off_topic_output_ratings[urim] == True:
                true_positives.append(urim) 

        elif gold_standard_urim_topic_ratings[urim] == False \
            and off_topic_output_ratings[urim] == False:
                true_negatives.append(urim)

        elif gold_standard_urim_topic_ratings[urim] == True \
            and off_topic_output_ratings[urim] == False:
                false_negatives.append(urim)

        elif gold_standard_urim_topic_ratings[urim] == False \
            and off_topic_output_ratings[urim] == True:
                false_positives.append(urim)


    print("TP: {}".format(len(true_positives)))
    print("TN: {}".format(len(true_negatives)))
    print("FP: {}".format(len(false_positives)))
    print("FN: {}".format(len(false_negatives)))
