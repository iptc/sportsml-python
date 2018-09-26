#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS, BaseObject
from .sports_metadata import SportsMetadata
from .event_metadata import EventMetadata
from .base_metadata import CommonAttributes


class Actions(BaseObject):
    actions = []

    def __init__(self, xmlelement=None, **kwargs):
        super(Actions, self).__init__(**kwargs)
        self.actions = []
        if type(xmlelement) == etree.Element:
            for childelem in xmlelement:
                action = Action(xmlelement=childelem)
                self.actions.append(action)

    def as_dict(self):
        return [ a.as_dict() for a in self.actions ]

    def __bool__(self):
        return len(self.actions) != 0


class BaseEventStateAttributeGroup(BaseObject):
    dict = {}
    # Number of minutes that have elapsed since the beginning of the game.
    minutes_elapsed = None
    # The time elapsed, but only given as whole minutes.
    period_minute_elapsed = None
    # The time elapsed in the current period.
    period_time_elapsed = None
    # The time remaining in the current period.
    period_time_remaining = None

    def __init__(self, xmlelement=None, **kwargs):
        self.dict = {}
        super(BaseEventStateAttributeGroup, self).__init__(**kwargs)
        if type(xmlelement) == etree.Element:
            self.minutes_elapsed = xmlelement.get('minutes-elapsed')
            self.period_minute_elapsed = xmlelement.get('period-minute-elapsed')
            self.period_time_elapsed = xmlelement.get('period-time-elapsed')
            self.period_time_remaining = xmlelement.get('period-time-remaining')

    def as_dict(self):
        super(BaseEventStateAttributeGroup, self).as_dict()
        if self.minutes_elapsed:
            self.dict.update({ 'minutesElapsed': self.minutes_elapsed })
        if self.period_minute_elapsed:
            self.dict.update({ 'periodMinuteElapsed': self.period_minute_elapsed })
        if self.period_time_elapsed:
            self.dict.update({ 'periodTimeElapsed': self.period_time_elapsed })
        if self.period_time_remaining:
            self.dict.update({ 'periodTimeRemaining': self.period_time_remaining })
        return self.dict


class ActionAttributes(CommonAttributes, BaseEventStateAttributeGroup):
    # This is considered the "current" team in action
    team_idref = None
    # This is the opposing team, if any
    opposing_team_idref = None
    # Date and time when this play/action record was created.
    # This would be the record from the reporter's data entry system.
    created = None
    # Date and time when this play/action record was last modified.
    # This would be the record from the reporter's data entry system.
    last_modified = None
    # Date and time when this play/action took place on the field.
    date_time = None
    # The result of the play or action.
    # See "result" SportsML vocabs for various sports:
    # http://cv.iptc.org/newscodes/spamfresult/
    # http://cv.iptc.org/newscodes/spsocresult/
    result = None
    # Sequence-number. Should be separate sequences for sub-actions inside an action
    sequence_number = None
    # Textual comment of the action
    comment = None
    # The type of competitive action taken on the field of play.
    # See "action" SportsML vocabs for various sports:
    # http://cv.iptc.org/newscodes/spamfaction/
    # http://cv.iptc.org/newscodes/spbblaction/
    # http://cv.iptc.org/newscodes/spbkbaction/
    # http://cv.iptc.org/newscodes/spichaction/
    # http://cv.iptc.org/newscodes/spmcraction/
    # http://cv.iptc.org/newscodes/rgxaction/
    # http://cv.iptc.org/newscodes/spsocaction/
    # http://cv.iptc.org/newscodes/sptenaction/
    type = None
    # Total time elapsed of event
    time_elapsed = None
    # Time remaining of event
    time_remaining = None
    # Number of players in the "current" team
    player_count = None
    # Number of players in the opposing team
    player_count_opposing = None
    # A string indicating where on the court the action began.
    # Could be an approximate region, or a more complex value adhering to some elaborate coordinate system.
    start_location = None
    # A string indicating where on the court the action occured.
    # Could be an approximate region, or a more complex value adhering to some elaborate coordinate system.
    end_location = None
    # The zone on the playing field where the action took place.
    # qcoded value that can be sport specific
    zone = None
    # Time remaining of powerplay
    power_play_time_remaining = None
    # Number of players more on the team in power play, also see the player count attributes
    power_play_advantage = None
    # Who called the timeout, either team or official. ID is given under participant.
    # SportsML vocab uri: http://cv.iptc.org/newscodes/spamfcaller/
    caller_type = None
    # Even strength, power play, short handed, etc.
    # SportsML vocab uri: http://cv.iptc.org/newscodes/spichstrength/
    strength = None
    # How many points this score was worth for the scoring team.
    points = None
    # How the initiative changed. Steal, lost-ball etc.
    turnover_type = None
    # Number or name of current period of event. Normally a number but can be things like OT etc
    period_value = None
    # Length of current period of event
    period_length = None
    # Score of the "current" team
    score_team = None
    # Score of the opposing team
    score_team_opposing = None
    # Timeouts left for the "current" team
    timeouts_left = None
    # Length of timeout
    timeout_duration = None
    # Type of timeout.
    # SportsML vocab uri: http://cv.iptc.org/newscodes/spamftimeout/
    timeout_type = None
    # The type of score for sports with more than one way to gain points
    # (e.g. american-football) in which every play is a score attempt.
    # For other sports use score-attempt-type.
    # SportsML vocab uri: http://cv.iptc.org/newscodes/spamfscore/
    score_type = None
    save_type = None
    save_method = None
    pass_type = None
    pass_description = None
    pass_method = None
    # The type of shot taken. See "shot"
    # SportsML vocabs for various sports:
    # http://cv.iptc.org/newscodes/spgolshot/
    # http://cv.iptc.org/newscodes/sptenshot/
    # http://cv.iptc.org/newscodes/spcurshot/
    shot_type = None
    shot_distance = None
    # SportsML vocab uri: http://cv.iptc.org/newscodes/spdistanceunits/
    shot_distance_units = None
    # The name of the type of penalty. See "penalty" SportsML vocabs for various sports:
    # http://cv.iptc.org/newscodes/spamfpenalty/
    # http://cv.iptc.org/newscodes/spichpenalty/
    # http://cv.iptc.org/newscodes/sprgxpenalty/
    # http://cv.iptc.org/newscodes/spsocpenalty/
    penalty_type = None
    # The degree of punishment for the penalty eg. yellow or red card, major, minor,
    # game misconduct, etc. See "penaltylevel" SportsML vocabs for various sports:
    # http://cv.iptc.org/newscodes/spbkbpenaltylevel/
    # http://cv.iptc.org/newscodes/spichpenaltylevel/
    # http://cv.iptc.org/newscodes/sprgxpenaltylevel/
    # http://cv.iptc.org/newscodes/spsocpenaltylevel/
    penalty_level = None
    # What the foul resulted in. See "penaltyresult" SportsML vocabs for various sports:
    # http://cv.iptc.org/newscodes/sprgxpenaltyresult/
    # http://cv.iptc.org/newscodes/spsocpenaltyresult/
    penalty_result = None
    # Which side committed the penalty, usually offense or defense.
    # SportsML vocab uri: http://cv.iptc.org/newscodes/sppenaltyside/
    penalty_side = None
    # The length of this penalty. Normally in minutes, but could be rest of the game etc
    penalty_length = None
    # The name of the penalty
    penalty_name = None
    # The sum of penalties recieved by this team/participant this event
    penalty_count = None
    # If this action marks the start or the end of the penalty time: enum "start" or "end"
    penalty_status = None
    # Whether the receiver of the penalty was the team, the player, a coach, a ref, etc.
    # SportsML vocab uri: http://cv.iptc.org/newscodes/sprecipienttype/
    recipient_type = None
    # The type of score that was attempted.
    # See "scoreattempt" SportsML vocabs for various sports:
    # http://cv.iptc.org/newscodes/spbkbscoreattempt/
    # http://cv.iptc.org/newscodes/spichscoreattempt/
    # http://cv.iptc.org/newscodes/sprgxscoreattempt/
    # http://cv.iptc.org/newscodes/spsocscoreattempt/
    score_attempt_type = None
    # The result of the score attempt eg. blocked, missed, etc.
    # See "scoreattemptresult" SportsML vocabs for various sports:
    # http://cv.iptc.org/newscodes/spbkbscoreattemptresult/
    # http://cv.iptc.org/newscodes/spichscoreattemtresult/
    # http://cv.iptc.org/newscodes/sprgxscoreattemptresult/
    # http://cv.iptc.org/newscodes/spsocscoreattemptresult/ 
    score_attempt_result = None
    # Side of the body of the player attempting to score
    score_attempt_side = None
    # What part of the body or equipment the player used to attempt to score.
    # See "scoreattemptmethod" SportsML vocabs for various sports:
    # http://cv.iptc.org/newscodes/spsocscoreattemptmethod/
    score_attempt_method = None
    score_attempt_situation = None
    # Part of the goal where the score or score-attempt was aimed.
    goal_zone = None
    # Angle on the field of the play.
    angle = None
    # Distance on the field of the play.
    distance = None
    # Body part used to perform an action.
    body_part = None
    # Recommended x,y 0-100. The location of the action on the field of play represented as a grid.
    field_location = None
    # Recommended x,y 0-100. The location on goal-mouth grid in which the ball/puck entered.
    goal_location = None
    # time added to period.
    time_addition = None
    # When this shot was taken, amongst all the shootout shots of a game for
    # one particular team. For example: 3 (if it was the third shot of the shootout). 
    shootout_shot_order = None
    # also used to show winner of jumpball in basket.
    faceoff_winner = None
    # The reason for the substitution of a player
    substitution_reason = None

    #def __init__(self, xmlelement=None, **kwargs):
    def __init__(self, **kwargs):
        super(ActionAttributes, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.team_idref = xmlelement.get('team-idref')
            self.opposing_team_idref = xmlelement.get('opposing_team_idref')
            self.created = xmlelement.get('created')
            self.last_modified = xmlelement.get('last-modified')
            self.date_time = xmlelement.get('date-time')
            self.result = xmlelement.get('result')
            self.sequence_number = xmlelement.get('sequence-number')
            self.comment = xmlelement.get('comment')
            self.type = xmlelement.get('type')
            self.time_elapsed = xmlelement.get('time-elapsed')
            self.time_remaining = xmlelement.get('time-remaining')
            self.player_count = xmlelement.get('player-count')
            self.player_count_opposing = xmlelement.get('player-count-opposing')
            self.start_location = xmlelement.get('start-location')
            self.end_location = xmlelement.get('end-location')
            self.zone = xmlelement.get('zone')
            self.power_play_time_remaining = xmlelement.get('power-play-time-remaining')
            self.power_play_advantage = xmlelement.get('power-play-advantage')
            self.caller_type = xmlelement.get('caller-type')
            self.strength = xmlelement.get('strength')
            self.points = xmlelement.get('points')
            self.turnover_type = xmlelement.get('turnover-type')
            self.period_value = xmlelement.get('period-value')
            self.period_length = xmlelement.get('period-length')
            self.score_team = xmlelement.get('score-team')
            self.score_team_opposing = xmlelement.get('score-team-opposing')
            self.timeouts_left = xmlelement.get('timeouts-left')
            self.timeout_duration = xmlelement.get('timeout-duration')
            self.timeout_type = xmlelement.get('timeout-type')
            self.score_type = xmlelement.get('score-type')
            self.save_type = xmlelement.get('save-type')
            self.save_method = xmlelement.get('save-method')
            self.pass_type = xmlelement.get('pass-type')
            self.pass_description = xmlelement.get('pass-description')
            self.pass_method = xmlelement.get('pass-method')
            self.shot_type = xmlelement.get('shot-type')
            self.shot_distance = xmlelement.get('shot-distance')
            self.shot_distance_units = xmlelement.get('shot-distance-units')
            self.penalty_type = xmlelement.get('penalty-type')
            self.penalty_level = xmlelement.get('penalty-level')
            self.penalty_result = xmlelement.get('penalty-result')
            self.penalty_side = xmlelement.get('penalty-side')
            self.penalty_length = xmlelement.get('penalty-length')
            self.penalty_name = xmlelement.get('penalty-name')
            self.penalty_count = xmlelement.get('penalty-count')
            self.penalty_status = xmlelement.get('penalty-status')
            self.recipient_type = xmlelement.get('recipient-type')
            self.score_attempt_type = xmlelement.get('score-attempt-type')
            self.score_attempt_result = xmlelement.get('score-attempt-result')
            self.score_attempt_side = xmlelement.get('score-attempt-side')
            self.score_attempt_method = xmlelement.get('score-attempt-method')
            self.score_attempt_situation = xmlelement.get('score-attempt-situation')
            self.goal_zone = xmlelement.get('goal-zone')
            self.angle = xmlelement.get('angle')
            self.distance = xmlelement.get('distance')
            self.body_part = xmlelement.get('body-part')
            self.field_location = xmlelement.get('field-location')
            self.goal_location = xmlelement.get('goal-location')
            self.time_addition = xmlelement.get('time-addition')
            self.shootout_shot_order = xmlelement.get('shootout-shot-order')
            self.faceoff_winner = xmlelement.get('faceoff-winner')
            self.substitution_reason = xmlelement.get('substitution-reason')

    def as_dict(self):
        super(ActionAttributes, self).as_dict()
        if self.team_idref:
            self.dict.update({'teamIdref': self.team_idref})
        if self.opposing_team_idref:
            self.dict.update({'opposingTeamIdref': self.opposing_team_idref })
        if self.created:
            self.dict.update({'created': self.created})
        if self.last_modified:
            self.dict.update({'lastModified': self.last-modified})
        if self.date_time:
            self.dict.update({'dateTime': self.date-time })
        if self.result:
            self.dict.update({'result': self.result})
        if self.sequence_number:
            self.dict.update({'sequence-number': self.sequence_number })
        if self.comment:
            self.dict.update({'comment': self.comment })
        if self.type:
            self.dict.update({'type': self.type })
        if self.time_elapsed:
            self.dict.update({'timeElapsed': self.time_elapsed })
        if self.time_remaining:
            self.dict.update({'timeRemaining': self.time_remaining })
        if self.player_count:
            self.dict.update({'playerCount': self.player_count })
        if self.player_count_opposing:
            self.dict.update({'playerCountOpposing': self.player_count_opposing })
        if self.start_location:
            self.dict.update({'startLocation': self.start_location })
        if self.end_location:
            self.dict.update({'endLocation': self.end_location })
        if self.zone:
            self.dict.update({'zone': self.zone })
        if self.power_play_time_remaining:
            self.dict.update({'powerPlayTimeRemaining': self.power_play_time_remaining })
        if self.power_play_advantage:
            self.dict.update({'powerPlayAdvantage': self.power_play_advantage })
        if self.caller_type:
            self.dict.update({'caller-type': self.caller_type })
        if self.strength:
            self.dict.update({'strength': self.strength })
        if self.points:
            self.dict.update({'points': self.points })
        if self.turnover_type:
            self.dict.update({'turnover-type': self.turnover_type })
        if self.period_value:
            self.dict.update({'period-value': self.period_value })
        if self.period_length:
            self.dict.update({'period-length': self.period_length })
        if self.score_team:
            self.dict.update({'score-team': self.score_team })
        if self.score_team_opposing:
            self.dict.update({'score-team-opposing': self.score_team_opposing })
        if self.timeouts_left:
            self.dict.update({'timeouts-left': self.timeouts_left })
        if self.timeout_duration:
            self.dict.update({'timeout-duration': self.timeout_duration })
        if self.timeout_type:
            self.dict.update({'timeout-type': self.timeout_type })
        if self.score_type:
            self.dict.update({'score-type': self.score_type })
        if self.save_type:
            self.dict.update({'save-type': self.save_type })
        if self.save_method:
            self.dict.update({'save-method': self.save_method })
        if self.pass_type:
            self.dict.update({'pass-type': self.pass_type })
        if self.pass_description:
            self.dict.update({'pass-description': self.pass_description })
        if self.pass_method:
            self.dict.update({'pass-method': self.pass_method })
        if self.shot_type:
            self.dict.update({'shot-type': self.shot_type })
        if self.shot_distance:
            self.dict.update({'shot-distance': self.shot_distance })
        if self.shot_distance_units:
            self.dict.update({'shot-distance-units': self.shot_distance_units})
        if self.penalty_type:
            self.dict.update({ 'penaltyType': self.penalty_type })
        if self.penalty_level:
            self.dict.update({ 'penaltyLevel': self.penalty_level })
        if self.penalty_result:
            self.dict.update({ 'penaltyLevel': self.penalty_result })
        if self.penalty_side:
            self.dict.update({ 'penaltySide': self.penalty_side })
        if self.penalty_length:
            self.dict.update({ 'penaltyLength': self.penalty_length })
        if self.penalty_name:
            self.dict.update({ 'penaltyName': self.penalty_name })
        if self.penalty_count:
            self.dict.update({ 'penaltyCount': self.penalty_count })
        if self.penalty_status:
            self.dict.update({ 'penaltyStatus': self.penalty_status })
        if self.recipient_type:
            self.dict.update({ 'recipientType': self.recipient_type })
        if self.score_attempt_type:
            self.dict.update({ 'scoreAttemptType': self.score_attempt_type })
        if self.score_attempt_result:
            self.dict.update({ 'scoreAttemptResult': self.score_attempt_result })
        if self.score_attempt_side:
            self.dict.update({ 'scoreAttemptSide': self.score_attempt_side })
        if self.score_attempt_method:
            self.dict.update({ 'scoreAttemptMethod': self.score_attempt_method })
        if self.score_attempt_situation:
            self.dict.update({ 'scoreAttemptSituation': self.score_attempt_situation })
        if self.goal_zone:
            self.dict.update({ 'goalZone': self.goal_zone })
        if self.angle:
            self.dict.update({ 'angle': self.angle })
        if self.distance:
            self.dict.update({ 'distance': self.distance })
        if self.body_part:
            self.dict.update({ 'bodyPart': self.body_part })
        if self.field_location:
            self.dict.update({ 'fieldLocation': self.field_location })
        if self.goal_location:
            self.dict.update({ 'goalLocation': self.goal_location })
        if self.time_addition:
            self.dict.update({ 'timeAddition': self.time_addition })
        if self.shootout_shot_order:
            self.dict.update({ 'shootoutShotOrder': self.shootout_shot_order })
        if self.faceoff_winner:
            self.dict.update({ 'faceoffWinner': self.faceoff_winner })
        if self.substitution_reason:
            self.dict.update({ 'substitutionReason': self.substitution_reason })

        return self.dict

    """
        TODO:
        <xs:attributeGroup ref="americanFootballActionAttributes"/>
        <xs:attributeGroup ref="baseballActionAttributes"/>
        <xs:attributeGroup ref="curlingActionAttributes"/>
        <xs:attributeGroup ref="golfActionAttributes"/>
        <xs:attributeGroup ref="motorRacingActionAttributes"/>
        <xs:attributeGroup ref="soccerActionAttributes"/>
        <xs:attributeGroup ref="tennisActionAttributes"/>
    """


class Action(ActionAttributes):
    """
    Any number of action inside the actions holder. An action can have any number of sub-actions.
    """
    dict = {}
    sub_actions = None
    participants = None

    #def __init__(self, xmlelement=None, **kwargs):
    def __init__(self, **kwargs):
        super(Action, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.sub_actions = Actions(
                xmlelement.findall(NEWSMLG2_NS+'action')
            )
            self.participants = Participants(
                xmlelement.findall(NEWSMLG2_NS+'participant')
            )

    def as_dict(self):
        dict = super(Action, self).as_dict()
        # FIXME recursion error
        #if self.sub_actions:
        #    dict.update({ 'actions': self.sub_actions.as_dict() })
        if self.participants:
            self.dict.update({ 'participants': self.participants.as_dict() })
        return self.dict


class Participants(BaseObject):
    participants = []

    def __init__(self, xmlarray=None, **kwargs):
        self.participants = []
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                participant = Participant(xmlelement=xmlelement)
                self.participants.append(participant)

    def as_dict(self):
        return [ p.as_dict() for p in self.participants ]


class CommonParticipantAttributes(BaseObject):
    # A pointer to a player who participated in the play.
    idref = None
    # A pointer to the participant's team.
    team_idref = None
    # The role of the participant in the particular action,
    # as opposed to their designated position on the team.
    role = None

    # def __init__(self, xmlelement=None, **kwargs):
    def __init__(self, **kwargs):
        super(CommonParticipantAttributes, self).__init__(**kwargs)
        if 'xmlelement' in kwargs and type(kwargs['xmlelement']) == etree.Element:
            self.idref = kwargs['xmlelement'].get('idref')
            self.team_idref = kwargs['xmlelement'].get('team_idref')
            self.role = kwargs['xmlelement'].get('role')

    def as_dict(self):
        super(CommonParticipantAttributes, self).as_dict()
        if self.idref:
            self.dict.update({ 'idref': self.idref })
        if self.team_idref:
            self.dict.update({ 'teamIdref': self.team_idref })
        if self.role:
            self.dict.update({ 'role': self.role })
        return self.dict


class CurlingParticipantAttributes(BaseObject):
    pass


class ParticipantAttributes(CommonParticipantAttributes,CurlingParticipantAttributes):
    """
    This object has no properties of its own, it just inherits from others
    """

    def __init__(self, **kwargs):
        super(ParticipantAttributes, self).__init__(**kwargs)

    def as_dict(self):
        super(ParticipantAttributes, self).as_dict()
        return dict


class Participant(CommonAttributes, ParticipantAttributes):
    """
    Base structure for a participant.
    """
    dict = {}
    # Recommended x,y 0-100.
    field_location = None
    # Total number goals at time of goal scored.
    goals_cumulative = None
    # Total number assists at time of assist scored.
    assists_cumulative = None
    lineup_slot = None
    yards_gained = None
    # Whether the participant in the play can be given credit for the goal or score.
    # enum: 1, 0
    score_credit = None

    def __init__(self, **kwargs):
        self.dict = {}
        super(Participant, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement', None)
        if type(xmlelement) == etree.Element:
            self.field_location = xmlelement.get('field-location')
            self.goals_cumulative = xmlelement.get('goals-cumulative')
            self.assists_cumulative = xmlelement.get('assists-cumulative')
            self.lineup_slot = xmlelement.get('lineup-slot')
            self.yards_gained = xmlelement.get('yards-gained')
            self.score_credit = xmlelement.get('score-credit')

    def as_dict(self):
        super(Participant, self).as_dict()
        if self.field_location:
            self.dict.update({ 'fieldLocation': self.field_location })
        if self.goals_cumulative:
            self.dict.update({ 'goalsCumulative': self.goals_cumulative })
        if self.assists_cumulative:
            self.dict.update({ 'assistsCumulative': self.assists_cumulative })
        if self.lineup_slot:
            self.dict.update({ 'lineupSlot': self.lineup_slot })
        if self.yards_gained:
            self.dict.update({ 'yardsGained': self.yards_gained })
        if self.score_credit:
            self.dict.update({ 'scoreCredit': self.score_credit })
        return self.dict
