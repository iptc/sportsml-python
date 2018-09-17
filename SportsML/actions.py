#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS
from .sports_metadata import SportsMetadata
from .event_metadata import EventMetadata
from .base_metadata import CommonAttributes, CoverageAttributes


class Actions(object):
    actions = []
    def __init__(self, xmlarray=None, **kwargs):
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                action = Action(xmlelement)
                self.actions.append(action)


class BaseEventStateAttributeGroup(object):
    """
    <xs:attributeGroup name="baseEventStateAttributeGroup">
        <xs:attribute name="minutes-elapsed" type="xs:string" use="optional">
            <xs:annotation>
                <xs:documentation>Number of minutes that have elapsed since the beginning of the game.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="period-minute-elapsed" type="xs:string" use="optional">
            <xs:annotation>
                <xs:documentation>The time elapsed, but only given as whole minutes.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="period-time-elapsed" type="xs:string" use="optional">
            <xs:annotation>
                <xs:documentation>The time elapsed in the current period.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="period-time-remaining" type="xs:string" use="optional">
            <xs:annotation>
                <xs:documentation>The time remaining in the current period.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:attributeGroup>
    """
    pass


class ActionAttributes(CommonAttributes, BaseEventStateAttributeGroup):
    """
        <xs:attribute name="team-idref" type="xs:string" use="optional">
            <xs:annotation>
                <xs:documentation>This is considered the "current" team in action</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="opposing-team-idref" type="xs:string" use="optional">
            <xs:annotation>
                <xs:documentation>This is the opposing team, if any</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="created" type="xs:dateTime" use="optional">
            <xs:annotation>
                <xs:documentation>Date and time when this play/action record was created. This would be the record from the reporter's data entry system.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="last-modified" type="xs:dateTime" use="optional">
            <xs:annotation>
                <xs:documentation>Date and time when this play/action record was last modified. This would be the record from the reporter's data entry system.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="date-time" type="xs:dateTime" use="optional">
            <xs:annotation>
                <xs:documentation>Date and time when this play/action took place on the field.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="result" use="optional" type="QCodeType">
            <xs:annotation>
                <xs:documentation>The result of the play or action. See "result" SportsML vocabs for various sports:
                    http://cv.iptc.org/newscodes/spamfresult/
                    http://cv.iptc.org/newscodes/spsocresult/
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="sequence-number" type="xs:integer" use="optional">
            <xs:annotation>
                <xs:documentation>Sequence-number. Should be separate sequences for sub-actions inside an action</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="comment" type="xs:string" use="optional">
            <xs:annotation>
                <xs:documentation>Textual comment of the action</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="type" type="QCodeType" use="optional">
            <xs:annotation>
                <xs:documentation>The type of competitive action taken on the field of play. See "action" SportsML vocabs for various sports:
                    http://cv.iptc.org/newscodes/spamfaction/
                    http://cv.iptc.org/newscodes/spbblaction/
                    http://cv.iptc.org/newscodes/spbkbaction/
                    http://cv.iptc.org/newscodes/spichaction/
                    http://cv.iptc.org/newscodes/spmcraction/
                    http://cv.iptc.org/newscodes/rgxaction/
                    http://cv.iptc.org/newscodes/spsocaction/
                    http://cv.iptc.org/newscodes/sptenaction/
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="time-elapsed" type="truncatedTimeType" use="optional">
            <xs:annotation>
                <xs:documentation>Total time elapsed of event</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="time-remaining" type="truncatedTimeType" use="optional">
            <xs:annotation>
                <xs:documentation>Time remaining of event</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="player-count" type="xs:integer" use="optional">
            <xs:annotation>
                <xs:documentation>Number of players in the "current" team</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="player-count-opposing" type="xs:integer" use="optional">
            <xs:annotation>
                <xs:documentation>Number of players in the opposing team</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="start-location" use="optional" type="xs:string">
            <xs:annotation>
                <xs:documentation>A string indicating where on the court the action began. Could be an approximate region, or a more complex value adhering to some elaborate coordinate system.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="end-location" use="optional" type="xs:string">
            <xs:annotation>
                <xs:documentation>A string indicating where on the court the action occured. Could be an approximate region, or a more complex value adhering to some elaborate coordinate system.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="zone" use="optional" type="QCodeType">
            <xs:annotation>
                <xs:documentation>The zone on the playing field where the action took place. qcoded value that can be sport specific</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="power-play-time-remaining" use="optional" type="truncatedTimeType">
            <xs:annotation>
                <xs:documentation>Time remaining of powerplay</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="power-play-advantage" use="optional" type="xs:nonNegativeInteger">
            <xs:annotation>
                <xs:documentation>Number of players more on the team in power play, also see the player count attributes</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="caller-type" use="optional" type="QCodeType">
            <xs:annotation>
                <xs:documentation>Who called the timeout, either team or official. ID is given under participant.  SportsML vocab uri: http://cv.iptc.org/newscodes/spamfcaller/ </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="strength" use="optional" type="QCodeType">
            <xs:annotation>
                <xs:documentation>Even strength, power play, short handed, etc.  SportsML vocab uri: http://cv.iptc.org/newscodes/spichstrength/ </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="points" use="optional" type="xs:integer">
            <xs:annotation>
                <xs:documentation>How many points this score was worth for the scoring team.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="turnover-type" use="optional" type="QCodeType">
            <xs:annotation>
                <xs:documentation>How the initiative changed. Steal, lost-ball etc.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="period-value" type="xs:string" use="optional">
            <xs:annotation>
                <xs:documentation>Number or name of current period of event. Normally a number but can be things like OT etc</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="period-length" type="truncatedTimeType" use="optional">
            <xs:annotation>
                <xs:documentation>Length of current period of event</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="score-team" type="xs:string" use="optional">
            <xs:annotation>
                <xs:documentation>Score of the "current" team</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="score-team-opposing" type="xs:string" use="optional">
            <xs:annotation>
                <xs:documentation>Score of the opposing team</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="timeouts-left" type="xs:integer" use="optional">
            <xs:annotation>
                <xs:documentation>Timeouts left for the "current" team</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="timeout-duration" type="xs:string" use="optional">
            <xs:annotation>
                <xs:documentation>Length of timeout</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="timeout-type" use="optional" type="QCodeType">
            <xs:annotation>
                <xs:documentation>Type of timeout. SportsML vocab uri: http://cv.iptc.org/newscodes/spamftimeout/</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="score-type" use="optional" type="QCodeType">
        <xs:annotation>
            <xs:documentation>The type of score for sports with more than one way to gain points (american-football) in which every play is a score attempt. For other sports use score-attempt-type. SportsML vocab uri: http://cv.iptc.org/newscodes/spamfscore/
            </xs:documentation>
        </xs:annotation>
        <xs:attribute name="save-type" use="optional" type="QCodeType"/>
        <xs:attribute name="save-method" use="optional" type="QCodeType"/>
        <xs:attribute name="pass-type" use="optional" type="QCodeType"/>
        <xs:attribute name="pass-description" use="optional" type="QCodeType"/>
        <xs:attribute name="pass-method" use="optional" type="QCodeType"/>
        <xs:attribute name="shot-type" use="optional" type="QCodeType">
            <xs:annotation>
                <xs:documentation>The type of shot taken. See "shot" SportsML vocabs for various sports:
                    http://cv.iptc.org/newscodes/spgolshot/
                    http://cv.iptc.org/newscodes/sptenshot/
                    http://cv.iptc.org/newscodes/spcurshot/
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="shot-distance" use="optional" type="xs:double"/>
        <xs:attribute name="shot-distance-units" type="QCodeType" use="optional">
            <xs:annotation>
                <xs:documentation>SportsML vocab uri: http://cv.iptc.org/newscodes/spdistanceunits/</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="penalty-type" use="optional" type="QCodeType">
            <xs:annotation>
                <xs:documentation>The name of the type of penalty. See "penalty" SportsML vocabs for various sports:
                    http://cv.iptc.org/newscodes/spamfpenalty/
                    http://cv.iptc.org/newscodes/spichpenalty/
                    http://cv.iptc.org/newscodes/sprgxpenalty/
                    http://cv.iptc.org/newscodes/spsocpenalty/
                </xs:documentation>
            </xs:annotation>
        <xs:attribute name="penalty-level" use="optional" type="QCodeType">
            <xs:annotation>
                <xs:documentation>The degree of punishment for the penalty eg. yellow or red card, major, minor, game misconduct, etc. See "penaltylevel" SportsML vocabs for various sports:
                    http://cv.iptc.org/newscodes/spbkbpenaltylevel/
                    http://cv.iptc.org/newscodes/spichpenaltylevel/
                    http://cv.iptc.org/newscodes/sprgxpenaltylevel/
                    http://cv.iptc.org/newscodes/spsocpenaltylevel/
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="penalty-result" use="optional" type="QCodeType">
            <xs:annotation>
                <xs:documentation>What the foul resulted in. See "penaltyresult" SportsML vocabs for various sports:
                    http://cv.iptc.org/newscodes/sprgxpenaltyresult/
                    http://cv.iptc.org/newscodes/spsocpenaltyresult/
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="penalty-side" type="QCodeType" use="optional">
            <xs:annotation>
                <xs:documentation>Which side committed the penalty, usually offense or defense. SportsML vocab uri: http://cv.iptc.org/newscodes/sppenaltyside/</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="penalty-length" use="optional" type="xs:string">
            <xs:annotation>
                <xs:documentation>The length of this penalty. Normally in minutes, but could be rest of the game etc</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="penalty-name" use="optional" type="xs:string">
            <xs:annotation>
                <xs:documentation>The name of the penalty</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="penalty-count" use="optional" type="xs:integer">
            <xs:annotation>
                <xs:documentation>The sum of penalties recieved by this team/participant this event</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="penalty-status" use="optional">
            <!-- If this action marks the start or the end of the penalty time -->
            <xs:simpleType id="penaltyStatus">
                <xs:restriction base="xs:string">
                    <xs:enumeration id="penaltyStatusStart" value="start"/>
                    <xs:enumeration id="penaltyStatusEnd" value="end"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="recipient-type" type="QCodeType" use="optional">
            <xs:annotation>
                <xs:documentation>Whether the receiver of the penalty was the team, the player, a coach, a ref, etc. SportsML vocab uri: http://cv.iptc.org/newscodes/sprecipienttype/</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="score-attempt-type" use="optional" type="QCodeType">
            <xs:annotation>
                <xs:documentation>The type of score that was attempted. See "scoreattempt" SportsML vocabs for various sports:
                    http://cv.iptc.org/newscodes/spbkbscoreattempt/
                    http://cv.iptc.org/newscodes/spichscoreattempt/
                    http://cv.iptc.org/newscodes/sprgxscoreattempt/
                    http://cv.iptc.org/newscodes/spsocscoreattempt/
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="score-attempt-result" use="optional" type="QCodeType">
            <xs:annotation>
                <xs:documentation>The result of the score attempt eg. blocked, missed, etc. See "scoreattemptresult" SportsML vocabs for various sports:
                    http://cv.iptc.org/newscodes/spbkbscoreattemptresult/
                    http://cv.iptc.org/newscodes/spichscoreattemtresult/
                    http://cv.iptc.org/newscodes/sprgxscoreattemptresult/
                    http://cv.iptc.org/newscodes/spsocscoreattemptresult/
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="score-attempt-side" use="optional" type="bodySideList">
            <xs:annotation>
                <xs:documentation>Side of the body of the player attempting to score</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="score-attempt-method" use="optional" type="QCodeType">
            <xs:annotation>
                <xs:documentation>What part of the body or equipment the player used to attempt to score. See "scoreattemptmethod" SportsML vocabs for various sports:
                    http://cv.iptc.org/newscodes/spsocscoreattemptmethod/
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="score-attempt-situation" use="optional" type="QCodeType"/>
        <xs:attribute name="goal-zone" use="optional" type="QCodeType">
            <xs:annotation>
                <xs:documentation>Part of the goal where the score or score-attempt was aimed.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="angle" use="optional" type="xs:string">
            <xs:annotation>
                <xs:documentation>Angle on the field of the play.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="distance" use="optional" type="xs:string">
            <xs:annotation>
                <xs:documentation>Angle on the field of the play.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="body-part" use="optional" type="QCodeType">
            <xs:annotation>
                <xs:documentation>Body part used to perform an action.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="field-location" use="optional" type="gridType">
            <xs:annotation>
                <xs:documentation>Recommended x,y 0-100. The location of the action on the field of play represented as a grid.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="goal-location" use="optional" type="gridType">
            <xs:annotation>
                <xs:documentation>Recommended x,y 0-100. The location on goal-mouth grid in which the ball/puck entered.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="time-addition" use="optional" type="xs:string">
            <xs:annotation>
                <xs:documentation>time added to period.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="shootout-shot-order" use="optional" type="xs:integer">
            <xs:annotation>
                <xs:documentation>When this shot was take, amongst all the shootout shots of a game for one particular team. For example: 3 (if it was the third shot of the shootout).</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="faceoff-winner" use="optional" type="xs:NCName">
            <xs:annotation>
                <xs:documentation>also used to show winner of jumpball in basket.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="substitution-reason" type="xs:string" use="optional"/>
        <!-- The reason for the substitution of a player -->

        <xs:attributeGroup ref="americanFootballActionAttributes"/>
        <xs:attributeGroup ref="baseballActionAttributes"/>
        <xs:attributeGroup ref="curlingActionAttributes"/>
        <xs:attributeGroup ref="golfActionAttributes"/>
        <xs:attributeGroup ref="motorRacingActionAttributes"/>
        <xs:attributeGroup ref="soccerActionAttributes"/>
        <xs:attributeGroup ref="tennisActionAttributes"/>
    """
    pass

class Action(ActionAttributes):
    # Any number of action inside the actions holder. An action can have any number of sub-actions.
    actions = None
    participants = None

    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            self.actions = Actions(
                xmlelement.findall(NEWSMLG2_NS+'action')
            )
            self.participants = Participants(
                xmlelement.findall(NEWSMLG2_NS+'participant')
            )


class Participants(object):
    participants = []

    def __init__(self, xmlarray=None, **kwargs):
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                participant = Participant(xmlelement)


class CommonParticipantAttributes(object):
    pass

class CurlingParticipantAttributes(object):
    pass

class ParticipantAttributes(CommonParticipantAttributes,CurlingParticipantAttributes):
    pass


class Participant(CommonAttributes, ParticipantAttributes):
    """
    Base structure for a participant.
    """
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

    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            self.field_location = xmlelement.get('field-location')
            self.goals_cumulative = xmlelement.get('goals-cumulative')
            self.assists_cumulative = xmlelement.get('assists-cumulative')
            self.lineup_slot = xmlelement.get('lineup-slot')
            self.yards_gained = xmlelement.get('yards-gained')
            self.score_credit = xmlelement.get('score-credit')
