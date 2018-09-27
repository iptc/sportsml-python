#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS, BaseObject, GenericArray
from .sports_metadata import SportsMetadata
from .event_metadata import EventMetadata
from .base_metadata import CommonAttributes


class BaseEventStateAttributeGroup(BaseObject):
    attributes = {
        # Number of minutes that have elapsed since the beginning of the game.
        'minutes-elapsed': 'minutesElapsed',
        # The time elapsed, but only given as whole minutes.
        'period-minute-elapsed': 'periodMinuteElapsed',
        # The time elapsed in the current period.
        'period-time-elapsed': 'periodTimeElapsed',
        # The time remaining in the current period.
        'period-time-remaining': 'periodTimeRemaining'
    }


class ActionAttributes(CommonAttributes, BaseEventStateAttributeGroup):
    attributes = {
        # This is considered the "current" team in action
        'team-idref': 'teamIdref',
        # This is the opposing team, if any
        'opposing-team-idref': 'opposingTeamIdref',
        # Date and time when this play/action record was created.
        # This would be the record from the reporter's data entry system.
        'created': 'created',
        # Date and time when this play/action record was last modified.
        # This would be the record from the reporter's data entry system.
        'last-modified': 'lastModified',
        # Date and time when this play/action took place on the field.
        'date-time': 'dateTime',
        # The result of the play or action.
        # See "result" SportsML vocabs for various sports:
        # http://cv.iptc.org/newscodes/spamfresult/
        # http://cv.iptc.org/newscodes/spsocresult/
        'result': 'result',
        # Sequence-number. Should be separate sequences for sub-actions inside an action
        'sequence_number': 'sequenceNumber',
        # Textual comment of the action
        'comment': 'comment',
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
        'type': 'type',
        # Total time elapsed of event
        'time-elapsed': 'timeElapsed',
        # Time remaining of event
        'time-remaining': 'timeRemaining',
        # Number of players in the "current" team
        'player-count': 'playerCount',
        # Number of players in the opposing team
        'player-count-opposing': 'playerCountOpposing',
        # A string indicating where on the court the action began.
        # Could be an approximate region, or a more complex value adhering to some elaborate coordinate system.
        'start-location': 'startLocation',
        # A string indicating where on the court the action occured.
        # Could be an approximate region, or a more complex value adhering to some elaborate coordinate system.
        'end-location': 'endLocation',
        # The zone on the playing field where the action took place.
        # qcoded value that can be sport specific
        'zone': 'zone',
        # Time remaining of powerplay
        'power-play-time-remaining': 'powerPlayTimeRemaining',
        # Number of players more on the team in power play, also see the player count attributes
        'power-play-advantage': 'powerPlayAdvantage',
        # Who called the timeout, either team or official. ID is given under participant.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/spamfcaller/
        'caller-type': 'callerType',
        # Even strength, power play, short handed, etc.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/spichstrength/
        'strength': 'strength',
        # How many points this score was worth for the scoring team.
        'points': 'points',
        # How the initiative changed. Steal, lost-ball etc.
        'turnover-type': 'turnoverType',
        # Number or name of current period of event. Normally a number but can be things like OT etc
        'period-value': 'periodValue',
        # Length of current period of event
        'period-length': 'periodLength',
        # Score of the "current" team
        'score-team': 'scoreTeam',
        # Score of the opposing team
        'score-team-opposing': 'scoreTeamOpposing',
        # Timeouts left for the "current" team
        'timeouts-left': 'timeoutsLeft',
        # Length of timeout
        'timeout-duration': 'timeoutDuration',
        # Type of timeout.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/spamftimeout/
        'timeout-type': 'timeoutType',
        # The type of score for sports with more than one way to gain points
        # (e.g. american-football) in which every play is a score attempt.
        # For other sports use score-attempt-type.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/spamfscore/
        'score-type': 'scoreType',
        'save-type': 'saveType',
        'save-method': 'saveMethod',
        'pass-type': 'passType',
        'pass-description': 'passDescription',
        'pass-method': 'passMethod',
        # The type of shot taken. See "shot"
        # SportsML vocabs for various sports:
        # http://cv.iptc.org/newscodes/spgolshot/
        # http://cv.iptc.org/newscodes/sptenshot/
        # http://cv.iptc.org/newscodes/spcurshot/
        'shot-type': 'shotType',
        'shot-distance': 'shotDistance',
        # SportsML vocab uri: http://cv.iptc.org/newscodes/spdistanceunits/
        'shot-distance-units': 'shotDistanceUnits',
        # The name of the type of penalty. See "penalty" SportsML vocabs for various sports:
        # http://cv.iptc.org/newscodes/spamfpenalty/
        # http://cv.iptc.org/newscodes/spichpenalty/
        # http://cv.iptc.org/newscodes/sprgxpenalty/
        # http://cv.iptc.org/newscodes/spsocpenalty/
        'penalty-type': 'penaltyType',
        # The degree of punishment for the penalty eg. yellow or red card, major, minor,
        # game misconduct, etc. See "penaltylevel" SportsML vocabs for various sports:
        # http://cv.iptc.org/newscodes/spbkbpenaltylevel/
        # http://cv.iptc.org/newscodes/spichpenaltylevel/
        # http://cv.iptc.org/newscodes/sprgxpenaltylevel/
        # http://cv.iptc.org/newscodes/spsocpenaltylevel/
        'penalty-level': 'penaltyLevel',
        # What the foul resulted in. See "penaltyresult" SportsML vocabs for various sports:
        # http://cv.iptc.org/newscodes/sprgxpenaltyresult/
        # http://cv.iptc.org/newscodes/spsocpenaltyresult/
        'penalty-result': 'penaltyResult',
        # Which side committed the penalty, usually offense or defense.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/sppenaltyside/
        'penalty-side': 'penaltySide',
        # The length of this penalty. Normally in minutes, but could be rest of the game etc
        'penalty-length': 'penaltyLength',
        # The name of the penalty
        'penalty-name': 'penaltyName',
        # The sum of penalties recieved by this team/participant this event
        'penalty-count': 'penaltyCount',
        # If this action marks the start or the end of the penalty time: enum "start" or "end"
        'penalty-status': 'penaltyStatus',
        # Whether the receiver of the penalty was the team, the player, a coach, a ref, etc.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/sprecipienttype/
        'recipient-type': 'recipientType',
        # The type of score that was attempted.
        # See "scoreattempt" SportsML vocabs for various sports:
        # http://cv.iptc.org/newscodes/spbkbscoreattempt/
        # http://cv.iptc.org/newscodes/spichscoreattempt/
        # http://cv.iptc.org/newscodes/sprgxscoreattempt/
        # http://cv.iptc.org/newscodes/spsocscoreattempt/
        'score-attempt-type': 'scoreAttemptType',
        # The result of the score attempt eg. blocked, missed, etc.
        # See "scoreattemptresult" SportsML vocabs for various sports:
        # http://cv.iptc.org/newscodes/spbkbscoreattemptresult/
        # http://cv.iptc.org/newscodes/spichscoreattemtresult/
        # http://cv.iptc.org/newscodes/sprgxscoreattemptresult/
        # http://cv.iptc.org/newscodes/spsocscoreattemptresult/
        'score-attempt-result': 'scoreAttemptResult',
        # Side of the body of the player attempting to score
        'score-attempt-side': 'scoreAttemptSide',
        # What part of the body or equipment the player used to attempt to score.
        # See "scoreattemptmethod" SportsML vocabs for various sports:
        # http://cv.iptc.org/newscodes/spsocscoreattemptmethod/
        'score-attempt-method': 'scoreAttemptMethod',
        'score-attempt-situation': 'scoreAttemptSituation',
        # Part of the goal where the score or score-attempt was aimed.
        'goal-zone': 'goalZone',
        # Angle on the field of the play.
        'angle': 'angle',
        # Distance on the field of the play.
        'distance': 'distance',
        # Body part used to perform an action.
        'body-part': 'bodyPart',
        # Recommended x,y 0-100. The location of the action on the field of play represented as a grid.
        'field-location': 'fieldLocation',
        # Recommended x,y 0-100. The location on goal-mouth grid in which the ball/puck entered.
        'goal-location': 'goalLocation',
        # time added to period.
        'time-addition': 'timeAddition',
        # When this shot was taken, amongst all the shootout shots of a game for
        # one particular team. For example: 3 (if it was the third shot of the shootout).
        'shootout-shot-order': 'shootoutShotOrder',
        # also used to show winner of jumpball in basket.
        'faceoff-winner': 'faceoffWinner',
        # The reason for the substitution of a player
        'substitution-reason': 'substitutionReason'
    }

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

    def __init__(self, **kwargs):
        super(Action, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            # sub-actions in another array
            self.sub_actions = Actions(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'action')
            )
            self.participants = Participants(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'participant')
            )

    def as_dict(self):
        dict = super(Action, self).as_dict()
        # FIXME recursion error
        #if self.sub_actions:
        #    dict.update({ 'actions': self.sub_actions.as_dict() })
        if self.participants:
            self.dict.update({ 'participants': self.participants.as_dict() })
        return self.dict


class Actions(GenericArray):
    """
    Array of Action objects.
    """
    element_class = Action


class CommonParticipantAttributes(BaseObject):
    attributes = {
        # A pointer to a player who participated in the play.
        'idref': 'idref',
        # A pointer to the participant's team.
        'team-idref': 'teamIdref',
        # The role of the participant in the particular action,
        # as opposed to their designated position on the team.
        'role': 'role'
    }


class CurlingParticipantAttributes(BaseObject):
    pass


class ParticipantAttributes(CommonParticipantAttributes,CurlingParticipantAttributes):
    """
    This object has no properties of its own, it just inherits from others
    """
    pass


class Participant(CommonAttributes, ParticipantAttributes):
    """
    Base structure for a participant.
    """
    attributes = {
        # Recommended x,y 0-100.
        'field_location': 'fieldLocation',
        # Total number goals at time of goal scored.
        'goals_cumulative': 'goalsCumulative',
        # Total number assists at time of assist scored.
        'assists_cumulative': 'assistsCumulative',
        'lineup_slot': 'lineupSlot',
        'yards_gained': 'yardsGained',
        # Whether the participant in the play can be given credit for the goal or score.
        # enum: 1, 0
        'score_credit': 'scoreCredit'
    }


class Participants(GenericArray):
    """
    Array of Participant objects.
    """
    element_class= Participant
