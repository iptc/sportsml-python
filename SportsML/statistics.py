#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS, BaseObject, GenericArray
from .base_metadata import CommonAttributes, CoverageAttributes, BaseMetadata
from .newsmlg2 import Names


class StatisticMetadata(BaseMetadata):
    """
    Identifies which teams are being covered.
    Also indicates the date ranges for which these stats cover.
    """
    pass


class Statistic(CommonAttributes, CoverageAttributes):
    """
    A table that generally compares the performance of teams or players.
    The fixture-key can identify which regulary-running statistics are being presented.
    Also appropriate for rosters (squad listings).
    """

    attributes = {
        # A code describing the class of statistic covered herein,
        # generally part of a controlled vocabulary.
        'type': 'type',
        # A display label for the enclosed statistical ranking.
        # (Should be placed as name in the metadata section.)
        'content-label': 'contentLabel'
    }

    def __init__(self, **kwargs):
        super(Statistic, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            from .entities import Groups, Teams, Players, Associates
            self.statistic_metadata = StatisticMetadata(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'statistic-metadata')
            )
            self.groups = Groups(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sports-property')
            )
            self.teams = Teams(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'team')
            )
            self.players = Players(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'player')
            )
            self.associates = Associates(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'associates')
            )
            self.status_changes = StatusChanges(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'status-change')
            )
 
    def as_dict(self):
        super(Statistic, self).as_dict()
        if self.statistic_metadata:
            self.dict.update({ 'statisticMetadata': self.statistic_metadata.as_dict() })
        if self.groups:
            self.dict.update({ 'groups': self.groups.as_dict() })
        if self.teams:
            self.dict.update({ 'teams': self.teams.as_dict() })
        if self.players:
            self.dict.update({ 'players': self.players.as_dict() })
        if self.associates:
            self.dict.update({ 'associates': self.associates.as_dict() })
        if self.status_changes:
            self.dict.update({ 'statusChanges': self.status_changes.as_dict() })
        return self.dict


class Statistics(GenericArray):
    """
    Array of Statistic objects.
    """
    element_class = Statistic


class BaseStats(CommonAttributes):
    """
    The very basic stats type for persons and teams.
    Extended by base2stats and used directly by officalstats.
    """
    ratings = None
    sports_properties = None
    stats = None

    def __init__(self, **kwargs):
        super(BaseStats, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.ratings = Ratings(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'rating')
            )
            self.sports_properties = Ratings(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sports-property')
            )
            self.stats = GenericStats(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'stats')
            )

    def as_dict(self):
        super(BaseStats, self).as_dict()
        if self.ratings:
            self.dict.update({ 'ratings': self.ratings.as_dict() })
        if self.sports_properties:
            self.dict.update({ 'sportsProperties': self.sports_properties.as_dict() })
        if self.stats:
            self.dict.update({ 'stats': self.stats.as_dict() })
        return self.dict
        

class GenericStatAttributes(BaseObject):
    """
    List of attributes used in generic stats
    """
    attributes = {
        # The sport to which the stats belong.
        'sport': 'sport',
        # The general classification of the stat within the sport eg ofensive, defensive, rebounding (basketball), special teams (american football).
        'class': 'class',
        # The formal identifier of the kind of stat.
        'stat-type': 'statType',
        # The formal type of the stat value eg. integer, string, etc.
        'value-type': 'valueType',
        # The value of the stat.
        'value': 'value'
    }


class GenericStat(GenericStatAttributes, CoverageAttributes):
    """
    A generic stat element that can be used together with or instead of
    more specific stat element and attributes. With nested stats the lower levels should
    be regarded as having the same value as their parents if that attribute is not
    specifically set.
    TODO implement this logic ^^ for nested stats
    """
    # The name of the stat.
    # SportsML names are same as attribute names of stats in the sport-specific plugins.
    names = None
    stats = None

    def __init__(self, **kwargs):
        super(GenericStat, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.names = Names(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'name')
            )
            self.stats = GenericStats(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'stat')
            )

    def as_dict(self):
        super(GenericStat, self).as_dict()
        if self.names:
            self.dict.update({ 'names': self.names.as_dict() })
        if self.stats:
            self.dict.update({ 'stats': self.stats.as_dict() })
        return self.dict


class GenericStats(GenericArray):
    """
    Array of GenericStat objects.
    """
    element_class = GenericStat


class OfficialStats(BaseStats):
    # inherits everything from BaseStats
    pass


class SubScore(BaseObject):
    # Statistics that detail the score for a particular period or inning.
    # Per-sport controlled vocabularies used for period-value.
    attributes = {
        # Generally a natural number. Could also be quarter-1, period-2, inning-5, etc.
        'period-value': 'periodValue',
        # The score for that period (or scoring unit).
        'score': 'score',
        # The type of sub-score.
        'sub-score-type': 'subScoreType',
        # The symbol for the sub-score unit.
        'sub-score-key': 'subScoreKey',
        # The name of the sub-score unit.
        'sub-score-name': 'subScoreName',
        # The ranking result of the sub-score unit.
        'rank': 'rank',
        # The running total during the sub-score period or unit. Good for split scores.
        'total-score': 'totalScore',
        # The attempts to score during the period (or scoring unit).
        'score-attempts': 'scoreAttempts'
    }


class SubScores(GenericArray):
    """
    Array of SubScore objects.
    """
    element_class = SubScore


class EventRecords(BaseObject):
    # TODO
    pass


class Ratings(BaseObject):
    # TODO
    pass


class SportsProperties(BaseObject):
    # TODO
    pass


class StatsSet(BaseObject):
    # TODO
    pass


class OutcomeTotals(BaseObject):
    # TODO
    pass


class OutcomeResults(BaseObject):
    # TODO
    pass


class Base2Stats(BaseStats):
    """
    Second level stats. Extends baseStats. Extended further in base3stats and used directly in associate
    """
    outcome_totals = None
    outcome_results = None
    attributes = {
        # Points accumulated by this associate.
        # For example, points earned by a NASCAR owner.
        'points': 'points'
    }
    attribute_types = {
        'points': 'integer'
    }

    def __init__(self, **kwargs):
        super(Base2Stats, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.outcome_totals = OutcomeTotals(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'outcome-total')
            )
            self.outcome_results = OutcomeResults(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'outcome-result')
            )

    def as_dict(self):
        super(Base2Stats, self).as_dict()
        if self.outcome_totals:
            self.dict.update({ 'outcomeTotals': self.outcome_totals.as_dict() })
        if self.outcome_results:
            self.dict.update({ 'outcomeResults': self.outcome_results.as_dict() })
        return self.dict


class PenaltyStats(CommonAttributes):
    """
    Statistics that detail the number of each type of penalty.
    Can be recorded for either a team or a player.
    """
    attributes = {
        # Could be a numeric value like 2, 5 or 10 for ice hockey, or yellow-card or red-card for soccer etc.
        'type': 'type',
        # The number of that type of penalities for this team or player.
        'count': 'count',
        # Amount penalized. Eg. total minutes (ice-hockey, lacrosse, etc.) or yards (american-football).
        'value': 'value'
    }
    attribute_types = {
        'count': 'integer'
    }


class PenaltyStatsSet(GenericArray):
    """
    Array of PenaltyStatsobjects.
    """
    element_class= PenaltyStats


class Ranks(BaseObject):
    # TODO
    pass


class StatAttributes(BaseObject):
    attributes = {
        # Final or current score of the team or player.
        'score': 'score',
        # Final or current score of the opposing team or player.
        'score_opposing': 'scoreOpposing',
        # Average per-game score for the team or player.
        'score_average': 'scoreAverage',
        # Average per-game score for the opposing team or player.
        'score_opposing_average': 'scoreOpposingAverage',
        # Describes how the score and score-opposing is valued.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/spscoreunits/
        'score_units': 'scoreUnits',
        # The points or time behind the leading score.
        'score_behind': 'scoreBehind',
        # Final or current number of attempts to score by a team or player. Example: in ice hockey, would represent total shots on goal.
        'score_attempts': 'scoreAttempts',
        # Final or current number of attempts to score by an opposing team or player.
        'score_attempts_opposing': 'scoreAttemptsOpposing',
        # A subset of score-attempts. Only counts those attempts that were on-goal.
        'score_attempts_on_goal': 'scoreAttemptsOnGoal',
        # Final or current number of attempts to score by an opposing team or player that were on-goal.
        'score_attempts_on_goal_opposing': 'scoreAttemptsOnGoalOpposing',
        # Percentage of attempted scores that reached their mark.
        'score_percentage': 'scorePercentage',
        # Percentage of attempted scores by opposing team or player that reached their mark.
        'score_percentage_opposing': 'scorePercentageOpposing',
        # Describes the effect that the result of the event or rank changing
        # has had on the team. Example: Whether or not a team has qualified for the
        # playoffs, or has been promoted or demoted to a different division.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/spresulteffect/
        'result_effect': 'resultEffect',
        # Whether the competitor won, lost, or tied.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/speventoutcome/
        'event_outcome': 'eventOutcome',
        # How many points were earned as a result of the outcome of this particular event.
        'event_standing_points': 'eventStandingPoints',
        # How many points were deducted as a result of the outcome of this particular event.
        # This occurs, for example, in the German Handball leagues.
        'event_standing_points_against': 'eventStandingPointsAgainst',
        # Qualifies "score" attribute.
        'score_type': 'scoreType',
        # Number of sports-events the player has yet to participate in.
        'events_remaining': 'eventsRemaining',
        # Amount of time the team or player has possession of ball (or similar object like puck).
        'time_of_possession': 'timeOfPossession',
        # Amount of time the team or player has possession of ball (or similar object like puck) expressed as a percentage of the full time of the match.
        'time_of_possession_percentage': 'timeOfPossessionPercentage',
        # Amount of time the opposing team or player has possession of ball (or similar object like puck) expressed as a percentage of the full time of the match.
        'time_of_possession_percentage_opposing': 'timeOfPossessionPercentageOpposing',
        # Amount of time the team or player has possession of ball (or similar object like puck) per game.
        'time_of_possession_average': 'timeOfPossessionAverage',
        # Amount of time the opposing team or player has possession of ball (or similar object like puck) per game.
        'time_of_possession_average_opposing': 'timeOfPossessionAverageOpposing',
        # Number of events in a series won by team or player.
        'series_score': 'seriesScore',
        # Number of events in a series won by opposing team or player.
        'series_score_opposing': 'seriesScoreOpposing',
        # The final score as adjusted by some authority. Usually as a result
        # of some dispute or transgression that must be settled post-event and rendered in
        # the score. Will differ from the regular score reflecting the number of actual
        # goals scored in play. Should be tested for before displaying actual
        # score.
        'adjusted_score_for': 'adjustedScoreFor',
        # The final score against as adjusted by some authority. Usually as
        # a result of some dispute or transgression that must be settled post-event and
        # rendered in the score. Will differ from the regular score reflecting the number
        # of actual goals scored in play. Should be tested for before displaying actual
        # score.
        'adjusted_score_against': 'adjustedScoreAgainst'
    }


class Base3Stats(Base2Stats, CoverageAttributes, StatAttributes):
    """
    Extends base2stats. Further extended in genericEntitystats. Used directly by groupStats
    """
    penalty_stats_set = None
    awards = None
    ranks = None

    def __init__(self, **kwargs):
        super(Base3Stats, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.penalty_stats_set = PenaltyStatsSet(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'penalty-stats')
            )
            from .sports_events import Awards
            self.awards = Awards(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'award')
            )
            self.ranks = Ranks(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'rank')
            )

    def as_dict(self):
        super(Base3Stats, self).as_dict()
        if self.penalty_stats_set:
            self.dict.update({ 'penaltyStats': self.penalty_stats_set.as_dict() })
        if self.awards:
            self.dict.update({ 'awards': self.awards.as_dict() })
        if self.ranks:
            self.dict.update({ 'ranks': self.ranks.as_dict() })
        return self.dict



class BaseGenericEntityStats(Base3Stats):
    """
    Statistics that apply to a team as a whole or a player.
    Not all stats are used in every sport.
    """
    sub_scores = None
    event_records = None
    attributes = {
        # The number of sports-events in which this team or player has already participated.
        'events-played': 'eventsPlayed',
        # Value for the amount of time played by the team or player over the
        # course of a particular time-span, such as a season.
        'time-played-total': 'timePlayedTotal'
    }
    attribute_types = {
        'events-played': 'integer'
    }
    
    def __init__(self, **kwargs):
        super(BaseGenericEntityStats, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.sub_scores = SubScores(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sub-score')
            )
            self.event_records = EventRecords(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'event-record')
            )

    def as_dict(self):
        super(BaseGenericEntityStats, self).as_dict()
        if self.sub_scores:
            self.dict.update({'subScores': self.sub_scores.as_dict()})
        if self.event_records:
            self.dict.update({'eventRecords': self.event_records.as_dict() })
        return self.dict


class BaseTeamStats(BaseGenericEntityStats):
    """
    Statistics that apply to the team as a whole.
    Not all stats are used in every sport.
    """
    pass  # only inherits from BaseGenericEntityStats


class TeamStats(BaseTeamStats):
    """ TODO
        <xs:element name="team-stats-american-football" type="americanFootballTeamStatsComplexType"/>
        <xs:element name="team-stats-baseball" type="baseballTeamStatsComplexType"/>
        <xs:element name="team-stats-basketball" type="basketballTeamStatsComplexType"/>
        <xs:element name="team-stats-ice-hockey" type="iceHockeyTeamStatsComplexType"/>
        <xs:element name="team-stats-soccer" type="soccerTeamStatsComplexType"/>
        <xs:element name="team-stats-tennis" type="tennisTeamStatsComplexType"/>
        <xs:element name="team-stats-motor-racing" type="motorRacingTeamStatsComplexType"/>
        <xs:element name="team-stats-curling" type="curlingTeamStatsComplexType"/>
        <xs:element name="team-stats-rugby" type="rugbyTeamStatsComplexType"/>
    """
    pass

class TeamStatsSet(GenericArray):
    """
    Array of TeamStats objects.
    """
    element_class = TeamStats


class BasePlayerStats(BaseGenericEntityStats):
    """
    Statistics that capture how a player has performed.
    Generally changes over the course of a sports-event.
    """
    attributes = {
        # Value for the amount of time played by this player in a particular sports-event.
        'time-played-event': 'timePlayed',
        # Value for the average amount of time played per-event by the player over the course of a particular time-span, such as a season.
        'time-played-event-average': 'timePlayedEventAverage',
        # Number of sports-events the player has played in since the start of the event.
        'events-started': 'eventsStarted',
        # Exact universal time player entered event. For example, the time a downhill skiier began a run.
        'date-time-entered': 'dateTimeEntered',
        # Exact universal time player exited event. For example, the time a downhill skiier finished a run.
        'date-time-exited': 'dateTimeExited',
        # Time player entered event expressed as conventional game-clock time. For example, the game minute a soccer player was subbed on to the field.
        'event-time-entered': 'eventTimeEntered',
        # Time player exited event expressed as conventional game-clock time. For example, the game minute a soccer player was subbed off the field.
        'event-time-exited': 'eventTimeExited'
    }
    attribute_types = {
        'events-started': 'integer'
    }


class PlayerStats(BasePlayerStats):

    def __init__(self, **kwargs):
        super(PlayerStats, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            pass

    """
    TODO: sport-specific player stats
                <xs:choice minOccurs="0">
                    <xs:element name="player-stats-american-football" type="americanFootballPlayerStatsComplexType"/>
                    <xs:element name="player-stats-baseball" type="baseballPlayerStatsComplexType"/>
                    <xs:element name="player-stats-basketball"  type="basketballPlayerStatsComplexType"/>
                    <xs:element name="player-stats-golf" type="golfPlayerStatsComplexType"/>
                    <xs:element name="player-stats-ice-hockey" type="iceHockeyPlayerStatsComplexType"/>
                    <xs:element name="player-stats-soccer" type="soccerPlayerStatsComplexType"/>
                    <xs:element name="player-stats-tennis" type="tennisPlayerStatsComplexType"/>
                    <xs:element name="player-stats-motor-racing" type="motorRacingPlayerStatsComplexType"/>
                    <xs:element name="player-stats-curling" type="curlingPlayerStatsComplexType"/>
                    <xs:element name="player-stats-rugby" type="rugbyPlayerStatsComplexType"/>
                    <!-- element ref="player-stats-alpineskiing" / -->
                </xs:choice>

    """
    def as_dict(self):
        super(PlayerStats, self).as_dict()
        return self.dict


class PlayerStatsSet(GenericArray):
    """
    Array of PlayerStats objects.
    """
    element_class = PlayerStats


class StatusChange(CommonAttributes, CoverageAttributes):
    """
    Indicates status change of an entity.
    """
    attributes = {
        # A pointer to the player or team that has undergone the status change.
        'changer-idref': 'changerIdRef',
        # What type of change was made in the status of a player or team.
        # Examples are injury, trade, cut.
        'status-change-type': 'statusChangeType',
        # What the original status of the player or team was.
        # Examples are active, inactive, disabled-list.
        'original-status': 'originalStatus',
        # What the new status of the player or team is.
        # Examples are active, inactive, disabled-list.
        'new-status': 'newStatus',
        # Generally, a pointer to the original team that the player in
        # changer-idref was affiliated with.
        'original-idref': 'originalIdRef',
        # Generally, a pointer to the new team that the player in
        # changer-idref is now affiliated with.
        'new-idref': 'newIdRef'
    }


class StatusChanges(GenericArray):
    """
    Set of StatusChange objects.
    """
    element_class = StatusChange


class WageringStats(BaseObject):
    def __init__(self, **kwargs):
        if type(xmlelement) == etree.Element:
            # TODO
            pass

    def as_dict(self):
        # TODO
        return None


class WageringStatsSet(GenericArray):
    """
    Array of WageringStats objects.
    """
    element_class = WageringStats
