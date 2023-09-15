class ThresholdError(Exception):
    pass


def predict_message_mood(message, model, bad_thresholds=0.3, good_thresholds=0.8):
    if good_thresholds < bad_thresholds or bad_thresholds < 0\
            or good_thresholds > 1:
        raise ThresholdError("invalid thresholds")
    pred = model.predict(message)
    verdict = "норм"
    if pred <= bad_thresholds:
        verdict = "неуд"
    elif pred >= good_thresholds:
        verdict = "отл"
    return verdict
