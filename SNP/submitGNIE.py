#WD
#Tested on Mac / python 3.6.5
#Assumes your VCF's to be sitting in subfolder VCF
import sys
import getopt
import os
import subprocess
def SNPsubmitter(inputfile):
    with open(inputfile) as vcfs:
        for line in vcfs:
            vcfline = line.strip().split(".")
            node = vcfline[1]
            outfolder = vcfline[0] + "_" + vcfline[1] + "_SNPGenie"
            gtf = node + '.gff'
            fasta = node + '.fasta'
            vcf = line.strip()
            print('Running SNPGenie on:' + vcf)
            bashcmd = "/data/leuven/318/vsc31803/Programs/snpgenie/snpgenie.pl --vcfformat=4 --fastafile=" + fasta +" --snpreport=" + vcf + " --gtffile=" + gtf
            process = subprocess.Popen(bashcmd, shell=True, stdout=subprocess.PIPE)
            process.wait()
            os.rename("SNPGenie_Results", outfolder)
            codres = outfolder + '/codon_results.txt'
            codres2 = outfolder + '/' + vcfline[0] + '_' + vcfline[1] + '_' + 'codon_results.txt'
            popsum = outfolder +'/population_summary.txt'
            popsum2 = outfolder +'/' + vcfline[0] + '_' + vcfline[1] + '_' + 'population_summary.txt'
            prodres = outfolder +'/product_results.txt'
            prodres2 = outfolder +'/' + vcfline[0] + '_' + vcfline[1] + '_' + 'product_results.txt'
            sitres = outfolder +'/site_results.txt'
            sitres2 = outfolder +'/' + vcfline[0] + '_' + vcfline[1] + '_' + 'site_results.txt'
            log = outfolder +'/SNPGenie_LOG.txt'
            log2 = outfolder + '/' + vcfline[0] + '_' + vcfline[1] + '_' + 'SNPGenie_LOG.txt'
            par = outfolder +'/SNPGenie_parameters.txt'
            par2 = outfolder + '/' + vcfline[0] + '_' + vcfline[1] + '_' + 'SNPGenie_parameters.txt'
            os.rename(codres,codres2)
            os.rename(popsum,popsum2)
            os.rename(prodres, prodres2)
            os.rename(sitres, sitres2)
            os.rename(log,log2)
            os.rename(par,par2)
def main(argv):
    inputfile = ''
    try:
        opts,args = getopt.getopt(argv,"h:i:", ["ifile="])
    except getopt.GetoptError:
        print('Need list of VCF files with format sample.node.vcf')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Need list of VCF files with format sample.node.vcf')
            sys.exit(2)
        if opt == '-i':
            inputfile = arg
    if inputfile == '':
        print('I need list of VCF files')
        sys.exit(2)
    SNPsubmitter(inputfile)
if __name__ == "__main__":
    main(sys.argv[1:])
