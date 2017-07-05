import java.util.*;
import java.io.*;


public class SeqLabel {


	public static ArrayList<FeatureSet> parseInputTrain(File input) {

		ArrayList<FeatureSet> set = new ArrayList<FeatureSet>();

		BufferedReader br = null;
		FeatureSet current = new FeatureSet();
//		int counter = 0;

		//read file
		try {
			br = new BufferedReader(new FileReader(input));
			for (String str = br.readLine(); str != null;str = br.readLine()) {
				if (str.equals("")){

					current = new FeatureSet();
					current.isLine = true;
					set.add(current);

				}
				else{
					String [] tokens = str.split("\t");
					current = new FeatureSet(tokens[0], tokens[1], tokens[2]);
					set.add(current);
				}
			}
		}
		catch (IOException e) {
			e.printStackTrace();
		}
		return set;
	}



public static ArrayList<FeatureSet> parseInputTest(File input) {

		ArrayList<FeatureSet> set = new ArrayList<FeatureSet>();

		BufferedReader br = null;
		FeatureSet current = new FeatureSet();

		//read file
		try {
			br = new BufferedReader(new FileReader(input));
			for (String str = br.readLine(); str != null;str = br.readLine()) {
				if (str.equals("")){
					current = new FeatureSet();
					current.isLine = true;
					set.add(current);

				}
				else{
					String [] tokens = str.split("\t");
					current = new FeatureSet(tokens[0], tokens[1]);
					set.add(current);
				}
			}
		}
		catch (IOException e) {
			e.printStackTrace();
		}
		return set;
	}



	public static ArrayList<FeatureSet> addFeatures(ArrayList<FeatureSet> set) {

		for (int i = 0; i < set.size(); i++) {
			FeatureSet curr = set.get(i);
			if (i > 0){
				curr.setPrevious(set.get(i-1).word, set.get(i-1).POS);
				if (i > 1){
					curr.twoWordsBack = set.get(i-2).word;
				}
			}
			if (i < set.size()-1){
				curr.setFollowing(set.get(i+1).word, set.get(i+1).POS);
				if (i < set.size()-2){
					curr.twoWordsForward = set.get(i+2).word;
				}
			}
			if (!curr.isLine) {
				//check for special characters
				// curr.hasSpecial   = !curr.word.matches("[A-Za-z0-9 ]*");
				curr.isAlpha   = curr.word.matches("[A-Za-z ]*");
				//check for capitalization
				if (curr.isAlpha) {
					curr.capitalized = !Character.isLowerCase(curr.word.charAt(0));
					curr.isCapital = curr.word.equals(curr.word.toUpperCase());
				}
			}
		}
		return set;
	}





	public static void outputTrain(ArrayList<FeatureSet> set, File output) throws IOException {
		FileWriter writer = new FileWriter(output);
		BufferedWriter bw = new BufferedWriter(writer);
		for (FeatureSet curr : set) {
			if (curr.isLine){
				bw.write("\n");
				continue;
			}
			bw.write(curr.word + "\t");
			bw.write("POS=" + curr.POS + "\t");
			bw.write(curr.getPrevious());
			bw.write(curr.getFollowing());
			// bw.write("Capitalized=" + curr.capitalized + "\t");
			// bw.write("IsCapital=" + curr.isCapital + "\t");
			// bw.write("Special_letters=" + curr.hasSpecial + "\t");
			bw.write("IsAlpha=" + curr.isAlpha + "\t");
			bw.write(curr.BIO);
			bw.write("\n");
		}
		bw.close();
	}

	public static void outputTest(ArrayList<FeatureSet> set, File output) throws IOException {
		FileWriter writer = new FileWriter(output);
		BufferedWriter bw = new BufferedWriter(writer);
		for (FeatureSet curr : set) {
			if (curr.isLine){
				bw.write("\n");
				continue;
			}
			bw.write(curr.word + "\t");
			bw.write("POS=" + curr.POS + "\t");
			bw.write(curr.getPrevious());
			bw.write(curr.getFollowing());
			// bw.write("Capitalized=" + curr.capitalized + "\t");
			// bw.write("IsCapital=" + curr.isCapital + "\t");
			// bw.write("Special_letters=" + curr.hasSpecial + "\t");
			bw.write("IsAlpha=" + curr.isAlpha + "\t");
			bw.write("\n");
		}
		bw.close();
	}


	public static void main(String[] args) throws IOException{

		boolean cont = true;

		while (cont) {

					Scanner reader = new Scanner(System.in);
					System.out.println("Enter input file name");
					String inputName = reader.nextLine();

					File input;
					File output;
					ArrayList<FeatureSet> trainingSet;
					ArrayList<FeatureSet> testSet;

					switch(inputName) {
						case ("WSJ_02-21.pos-chunk"):
								input = new File(inputName);
								trainingSet = addFeatures(parseInputTrain(input));
								output = new File("training.chunk");
								outputTrain(trainingSet, output);
								break;


						case ("WSJ_24.pos"):
								input = new File(inputName);
								testSet = addFeatures(parseInputTest(input));
								output = new File("test.chunk");
								outputTest(testSet, output);
								break;


						case ("WSJ_23.pos"):
								input = new File(inputName);
								testSet = addFeatures(parseInputTest(input));
								output = new File("WSJ_23.chunk");
								outputTest(testSet, output);
								break;

						default:
								System.out.println("Ending Noun Group tagger...");
								cont = false;
								break;


					}

		}

	}

}
