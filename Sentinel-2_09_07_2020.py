# -*- coding: utf-8 -*-
import ee
from ee_plugin import Map
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink)
from qgis import processing


class ExampleProcessingAlgorithm(QgsProcessingAlgorithm):
    """
    This is an example algorithm that takes a vector layer and
    creates a new identical one.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return ExampleProcessingAlgorithm()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Sentinel-2'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Sentinel-2')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Visualização de Sistemas Orbitais - ViSO SIPAM/CR-PV')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Visualização de Sistemas Orbitais - ViSO SIPAM/CR-PV'

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("Example algorithm short description")
        """
    def initAlgorithm(self, config=None):
        
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        

        # We add the input vector features source. It can have any kind of
        # geometry.
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input layer'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )

        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Output layer')
            )
        )
        """
    def processAlgorithm(self, parameters, context, feedback):
        
        collectt = ee.ImageCollection('COPERNICUS/S2_SR').filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 5)).filterDate('2019-09-15', '2019-12-30')
        median2019=collectt.median()
        S2_2019=median2019.divide(10000)
        
        collect = ee.ImageCollection('COPERNICUS/S2_SR').filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 5)).filterDate('2020-03-15', '2020-10-30')
        
        collecttt = ee.ImageCollection('COPERNICUS/S2_SR').filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 10)).filterDate('2020-01-15', '2020-03-05')

        medianatual=collect.median().divide(10000)
        medianJAN20=collecttt.median().divide(10000)

        
        Map.addLayer(S2_2019,{"bands": ['B4', 'B3', 'B2'], "min": 0.02, "max": 0.09, "gamma": 1}, 'Sentinel-2 Cor natural 2019 - Estiagem',0)
        Map.addLayer(S2_2019,{"bands": ['B11', 'B8', 'B4'], "min": 0.02, "max": 0.4}, 'Sentinel-2 Falsa Cor 2019 - Estiagem',0)
        
        Map.addLayer(medianatual,{"bands": ['B4', 'B3', 'B2'], "min": 0.02, "max": 0.09, "gamma": 1}, 'Sentinel-2 Cor natural 2020',0)
        Map.addLayer(medianJAN20,{"bands": ['B4', 'B3', 'B2'], "min": 0.02, "max": 0.09, "gamma": 1}, 'Sentinel-2 Cor natural JAN/FEV',0)
        Map.addLayer(medianJAN20,{"bands": ['B11', 'B8', 'B4'], "min": 0.02, "max": 0.4, "gamma": 1}, 'Sentinel-2 Falsa Cor JAN/FEV',0)
        Map.addLayer(medianatual,{"bands": ['B11', 'B8', 'B4'], "min": 0.02, "max": 0.4}, 'Sentinel-2 Falsa Cor 2020',0)
        Map.getCenter()
