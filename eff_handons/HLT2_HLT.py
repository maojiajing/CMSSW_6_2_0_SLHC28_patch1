# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: HLT2 --step=HLT:TutoEffcySession --era=Run2_2017 --data --conditions 92X_dataRun2_HLT_v7 --filein file:/afs/cern.ch/work/l/lathomas/public/HLTTutorial_27Oct2017/InputFiles/singlemuminiaod.root --secondfilein file:/afs/cern.ch/work/l/lathomas/public/HLTTutorial_27Oct2017/InputFiles/singlemuraw_1.root,file:/afs/cern.ch/work/l/lathomas/public/HLTTutorial_27Oct2017/InputFiles/singlemuraw_2.root,file:/afs/cern.ch/work/l/lathomas/public/HLTTutorial_27Oct2017/InputFiles/singlemuraw_3.root,file:/afs/cern.ch/work/l/lathomas/public/HLTTutorial_27Oct2017/InputFiles/singlemuraw_4.root,file:/afs/cern.ch/work/l/lathomas/public/HLTTutorial_27Oct2017/InputFiles/singlemuraw_5.root --processName=HLT2 -n 10000 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT2',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('HLTrigger.Configuration.HLT_TutoEffcySession_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/l/lathomas/public/HLTTutorial_27Oct2017/InputFiles/singlemuminiaod.root'),
    secondaryFileNames = cms.untracked.vstring('file:/afs/cern.ch/work/l/lathomas/public/HLTTutorial_27Oct2017/InputFiles/singlemuraw_1.root', 
        'file:/afs/cern.ch/work/l/lathomas/public/HLTTutorial_27Oct2017/InputFiles/singlemuraw_2.root', 
        'file:/afs/cern.ch/work/l/lathomas/public/HLTTutorial_27Oct2017/InputFiles/singlemuraw_3.root', 
        'file:/afs/cern.ch/work/l/lathomas/public/HLTTutorial_27Oct2017/InputFiles/singlemuraw_4.root', 
        'file:/afs/cern.ch/work/l/lathomas/public/HLTTutorial_27Oct2017/InputFiles/singlemuraw_5.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('HLT2 nevts:10000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('HLT2_HLT.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_dataRun2_HLT_v7', '')

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.demo = cms.EDAnalyzer('TriggerAnalyzerRAWMiniAOD')
process.TFileService = cms.Service("TFileService",
                                                   fileName = cms.string( "out.root" )
                                                                                      )
process.demo_step = cms.EndPath(process.demo)

# Schedule definition
process.schedule = cms.Schedule()
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.demo_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
