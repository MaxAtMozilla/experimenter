from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class BaseExperimentApplications(Enum):
    DESKTOP = "DESKTOP"
    FENIX = "FENIX"
    IOS = "IOS"
    KLAR = "KLAR_ANDROID"
    FOCUS = "FOCUS_ANDROID"


class BaseExperimentAudienceChannels(Enum):
    UNBRANDED = ("Unbranded",)
    NIGHTLY = ("Nightly",)
    BETA = ("Beta",)
    RELEASE = "Release"


@dataclass
class BaseExperimentBranchDataClass:
    name: str
    description: str
    feature_config: str


@dataclass
class BaseExperimentAudienceDataClass:
    channel: BaseExperimentAudienceChannels
    min_version: int
    targeting: Optional[str]
    percentage: float
    expected_clients: int
    locale: Optional[str]
    countries: Optional[str]


@dataclass
class BaseExperimentMetricsDataClass:
    primary_outcomes: Optional[List[str]]
    secondary_outcomes: Optional[List[str]]


@dataclass
class BaseExperimentDataClass:
    public_name: str
    hypothesis: str
    application: BaseExperimentApplications
    public_description: str
    branches: Optional[List[BaseExperimentBranchDataClass]]
    metrics: BaseExperimentMetricsDataClass
    audience: BaseExperimentAudienceDataClass